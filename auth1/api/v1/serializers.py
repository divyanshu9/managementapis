from rest_framework import serializers
from auth1.models import UserRole, UserDetail


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRole
        fields = "__all__"


class UserDetailSerializer(serializers.ModelSerializer):
    first_name = serializers.ReadOnlyField()
    last_name = serializers.ReadOnlyField()
    cases_involved = serializers.ReadOnlyField()

    class Meta:
        model = UserDetail
        fields = "__all__"
