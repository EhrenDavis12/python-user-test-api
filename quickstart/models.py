from django.db import models

# Create your models here.


class AppUser(models.Model):
    username = models.CharField(max_length=30)
    last_login = models.DateTimeField()
    login_count = models.IntegerField()
    project_count = models.IntegerField()
