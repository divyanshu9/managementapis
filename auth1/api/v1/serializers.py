from rest_framework import serializers
from auth1.models import UserRole


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRole
        fields = "__all__"
