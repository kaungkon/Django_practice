from django.db import models
from django.contrib.auth.models import User #authorized models theke userk import kora

#username, password, email
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    facebook_id = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __self__(self):
        return self.user.username
