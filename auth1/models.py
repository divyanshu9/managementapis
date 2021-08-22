from django.db import models
from django.contrib.auth.models import User
from common.mixins import TrackableMixin


class UserRole(TrackableMixin):
    name = models.CharField(max_length=50)


class UserDetail(TrackableMixin):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userdetails')
    location = models.CharField(max_length=250, blank=True)
    revenue = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    user_role = models.ForeignKey(UserRole, on_delete=models.CASCADE)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name
    
    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def cases_involved(self):
        return self.user.case.count()