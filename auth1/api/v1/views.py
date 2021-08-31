from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
import os

from sendgrid.helpers.mail import Mail
from sendgrid import SendGridAPIClient

from auth1.models import UserDetail, UserRole
from project.api.v1.serializers import CaseSerializer
from survey.api.v1.serializers import SurveyResponseSerializer, ResponseSerializer
from .utils import random_with_n_digits, random_with_n_aplha, get_tokens_for_user
from .serializers import UserRoleSerializer, UserDetailSerializer
from .filters import UserDetailFilter


sg = SendGridAPIClient(os.environ["SEND_GRID_KEY"])


class ChangePassword(APIView):

    def post(self, request):
        email = request.data.get("username")
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")
        reset_password = random_with_n_aplha(6)
        try:
            user_exists = User.objects.filter(username=email)
            if not user_exists.exists():
                return Response({"message": "User with this details not exists.", "flag": False},
                                status=status.HTTP_400_BAD_REQUEST)
            user_obj = user_exists.last()
            if not old_password:
                user_obj.set_password(reset_password)
                user_obj.save()
                message = Mail(from_email="wl@cmundp.de", to_emails=email,
                               subject='Password Reset',
                               html_content='<strong>Password: </strong>{}'.format(reset_password))
                sg.send(message)
                return Response({"message": "Password Sent on email", "flag": True},
                                status=status.HTTP_200_OK)
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
                    return Response({"message": "User Logged in", "id": user_obj.id, "token": user_token["access"], "username": user_obj.username, "flag": user_exists}, status=status.HTTP_200_OK)
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
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        location = request.data.get("location") or ""
        contact = request.data.get("contact") or ""
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
                user_detail = UserDetail.objects.create(user=user, user_role_id=user_role, location=location, contact=contact)
                #role = user_role.objects.get(id=user_role)
                if int(user_role) == 1:
                    survey = SurveyResponseSerializer(data=request.data.get("survey"))
                    responses = ResponseSerializer(data=request.data.get("survey")["responses"], many=True)
                    case = CaseSerializer(data=request.data.get("case"))
                    if survey.is_valid() and responses.is_valid():
                        print("is valid survey")
                        survey_response_obj = survey.save(submit_user=user)
                        responses = responses.save(survey_response=survey_response_obj)
                    else:
                        raise ValidationError(survey.errors)
                    if case.is_valid():
                        print("is valid case")
                        case_obj = case.save(client_user=user)
                    else:
                        raise ValidationError(case.errors)
            message = Mail(from_email="wl@cmundp.de", to_emails=email,
                           subject='Your one time password',
                           html_content='<strong>Password: </strong>{}'.format(password1))
            sg.send(message)
            return Response({"message": "Password sent on email"},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Please check the form filled."}, status=status.HTTP_400_BAD_REQUEST)


class UserRolesListAPIView(generics.ListAPIView):
    """
    User Roles List Api
    """
    serializer_class = UserRoleSerializer
    queryset = UserRole.objects.all().order_by("-id")


class UserRetrieveUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    User Retrieve Update and Destroy Api
    """
    serializer_class = UserDetailSerializer
    lookup_field = "user__id"
    queryset = UserDetail.objects.all().order_by("-id")


class UserDetailListAPIView(generics.ListAPIView):
    """
    Content Create and List Api
    """
    serializer_class = UserDetailSerializer
    filter_class = UserDetailFilter
    ordering_fields = ('id', 'location', 'status', 'user_role', ('name', 'user__first_name'), 'created_at')
    ordering = ['-id']
    queryset = UserDetail.objects.all()
