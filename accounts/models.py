from django.db import models
from django.contrib.auth.models import UserManager
# Create your models here.
from django.contrib.auth.models import AbstractUser
# from .managers import UserManager	
	
class myUser(AbstractUser):
	username = models.CharField(max_length=140,unique=True,default='2')
	
	status=models.IntegerField(default=0)

	
	USER_TYPE = (
		('seeker', 'Jobseeker'),
		('recruiters', 'Recruiters'),
		)
	user_types = models.CharField(
        max_length=10,
     
        choices=USER_TYPE,
        default='seeker'
    )

   
	USERNAME_FIELD = 'username'
