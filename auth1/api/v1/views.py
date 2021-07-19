from django.contrib.auth import authenticate
from django.shortcuts import render
from django.db import transaction
from rest_framework import status, generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.http import HttpResponse

from auth1.models import UserDetail, UserRole
from project.api.v1.serializers import CaseSerializer
from survey.api.v1.serializers import SurveyResponseSerializer, ResponseSerializer
from .utils import random_with_n_digits, random_with_n_aplha, get_tokens_for_user, geturl
from .serializers import UserRoleSerializer
#from .token import account_activation_token


class ChangePassword(APIView):

    def post(self, request):
        email = request.data.get("username")
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        try:
            user_exists = User.objects.filter(username=email)
            if not user_exists.exists():
                return Response({"message": "User with this details not exists.", "flag": False},
                                status=status.HTTP_400_BAD_REQUEST)
            user_obj = authenticate(username=user_exists[0].username, password=old_password)
            if user_obj:
                user_obj.set_password(new_password)
                user_obj.userdetails.status = True
                user_obj.userdetails.save()
                user_obj.save()
                return Response({"message": "Password changed", "flag": True},
                                status=status.HTTP_200_OK)
            else:
                return Response({"message": 'Password Incorrect', "flag": False},
                                status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(
                {'message': 'Please enter a valid username and password.', "details": str(e), "flag": False},
                status=status.HTTP_401_UNAUTHORIZED)


class Login(APIView):

    def post(self, request):
        name = request.data.get("username")
        password = request.data.get("password")
        try:
            user_exists = User.objects.filter(username=name)
            if not user_exists.exists():
                return Response({"message": "User with this details not exists.", "flag": False},
                                status=status.HTTP_400_BAD_REQUEST)
            user_obj = authenticate(username=user_exists[0].username, password=password)
            if user_obj:
                if user_obj.userdetails.status:
                    user_token = get_tokens_for_user(user_obj)
                    user_exists = UserDetail.objects.filter(user=user_obj).exists()
                    return Response({"message": "User Logged in", "token": user_token["access"], "username": user_obj.username, "flag": user_exists}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Please change your password.", "flag": False},
                                    status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({"message": 'Password Incorrect', "flag": False}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response(
                {'message': 'Please enter a valid username and password.', "details": str(e), "flag": False},
                status=status.HTTP_401_UNAUTHORIZED)


class Register(APIView):

    @transaction.atomic
    def post(self, request):
        #password1 = request.data.get("password")
        email = request.data.get("username")
        user_role = request.data.get("user_role")
        user_type = request.data.get("user_type")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        location = request.data.get("location")
        password1 = random_with_n_aplha(6)
        if email:
            user_exists = User.objects.filter(username=email).exists()
            user = None
            if user_exists:
                user = User.objects.get(username=email)
                if user.is_active:
                    return Response({"message": "User with this email already exists", "flag": False},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    print("setting password :", password1)
                    user.set_password(password1)
                    user.save()
            else:
                user = User.objects.create_user(username=email, password=password1, first_name=first_name,
                                                last_name=last_name)
                user_detail = UserDetail.objects.create(user=user, user_role_id=user_role, first_name=first_name,
                                                        last_name=last_name)
                if user_type == "M":
                    survey = SurveyResponseSerializer(data=request.data.get("survey"))
                    responses = ResponseSerializer(data=request.data.get("survey")["responses"], many=True)
                    case = CaseSerializer(data=request.data.get("case"))
                    if survey.is_valid() and responses.is_valid():
                        print("is valid survey")
                        survey_response_obj = survey.save(submit_user=user_detail)
                        responses = responses.save(survey_response=survey_response_obj)
                    else:
                        raise ValidationError(survey.errors)
                    if case.is_valid():
                        print("is valid case")
                        case_obj = case.save(client_user=user_detail)
                    else:
                        raise ValidationError(case.errors)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': str(urlsafe_base64_encode(force_bytes(user.pk))),
                'token': password1
                #'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(mail_subject, message, to=[email])
            email.send(fail_silently=False)
            return Response({"message": "Password sent on email"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Please check the form filled."}, status=status.HTTP_400_BAD_REQUEST)


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        api_url, site_url = geturl()
        return HttpResponse('Thank you for your email confirmation.'
                            ' Now you can login your account.Click'
                            ' <a href="%s/login">Here</a> to login.' % site_url)
    else:
        return HttpResponse('Activation link is invalid!')


class UserRolesListAPIView(generics.ListAPIView):
    """
    User Roles List Api
    """
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all().order_by("-id")
