from django.db import models
from accounts.models import myUser
# Create your models here.

class seekersdetails(models.Model):
    Id=models.ForeignKey(myUser,on_delete=models.CASCADE,default=2)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    Birth_date = models.DateField()
    City = models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Mobile_Number = models.IntegerField()
    Photo=models.FileField(default=0)
    secondary_school =models.CharField(max_length=100,default="")
    secondary_percent = models.FloatField(default=70)
    senior_school = models.CharField(max_length=100,default="")
    senior_percent = models.FloatField(default=70)
    College_name = models.CharField(max_length=100,default="M.B.M Engineering College")
    Stream = models.CharField(max_length=100,default="")
    Graduation_percent = models.IntegerField(default=70) 
    Skills = models.CharField(max_length=50,default="")
    exp_1 = models.CharField(max_length=50,default="")
    exp_1_about = models.CharField(max_length=100,default="")
    Resume=models.FileField(default=0) 
    
class recruitersdetail(models.Model):
    recruiter_id=models.ForeignKey(myUser,on_delete=models.CASCADE,default=2)
    Company_name = models.CharField(max_length=100)
    About=models.CharField(max_length=1000,default="abc")
    Mobile_Number = models.IntegerField()
    City = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    company_logo=models.FileField(default=0)
    
class posts(models.Model):
    recruiter_id=models.ForeignKey(myUser,on_delete=models.CASCADE,default=2)
    Post_name= models.CharField(max_length=100)
    Stream = models.CharField(max_length=100)
    Percent_Criteria = models.IntegerField()
    Salary = models.IntegerField()
    Experience= models.IntegerField()
    Vacancy = models.IntegerField()
    Deadline = models.DateField()

class Users_Apply(models.Model):
     Seekerid=models.ForeignKey(seekersdetails,on_delete=models.CASCADE,default=2)
     Companyid=models.ForeignKey(recruitersdetail,on_delete=models.CASCADE,default=2)
     Postid=models.ForeignKey(posts,on_delete=models.CASCADE,default=2)
     Apply=models.IntegerField(default=0)
   
        