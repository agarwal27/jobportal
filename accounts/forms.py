from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout,get_user_model
User = get_user_model()
class userloginform(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwagrs):
		username=self.cleaned_data.get('username')
		password=self.cleaned_data.get('password')
	
		if username and password:
			user=authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("this user does not exist")
			if not user.check_password(password):
				raise forms.ValidationError("password incorrect")
			if not user.is_active:
				raise forms.ValidationError("user is no longer active")
		return super(userloginform,self).clean(*args,**kwagrs)	


class UserRegisterForm(ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	

	class Meta:
		model=User
		fields=['username','email','password','user_types']






