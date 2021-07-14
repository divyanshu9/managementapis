from django.db import models
from django.contrib.auth.models import User
from common.mixins import TrackableMixin


class UserRole(TrackableMixin):
    name = models.CharField(max_length=50)


class UserDetail(TrackableMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userdetails')
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250, blank=True)
    status = models.BooleanField(default=False)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    
    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)