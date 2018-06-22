from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import recruitersdetail,seekersdetails,posts,Users_Apply
from django.forms import TextInput

class CompanyForm(ModelForm):
	
	class Meta:
		model=recruitersdetail
		widgets = {
			
			'Company_name': TextInput(attrs={'placeholder': 'Company Name'}),
			'Mobile_Number': TextInput(attrs={'placeholder': 'Mobile_Number'}),
			'About': TextInput(attrs={'placeholder': 'About'}),
			'City': TextInput(attrs={'placeholder': 'City'}),
			'Address': TextInput(attrs={'placeholder': 'Address'}),
		}
		exclude=('recruiter_id',)


class UserForm(ModelForm):
	
	class Meta:
		model=seekersdetails
		widgets = {
			'name': TextInput(attrs={'placeholder': 'Full Name'}),
			'City': TextInput(attrs={'placeholder': 'City'}),
			'Birth_date': TextInput(attrs={'placeholder': 'Birth date '}),
            'address': TextInput(attrs={'placeholder': 'Address '}),
            'State': TextInput(attrs={'placeholder': 'State '}),
			'Mobile_Number': TextInput(attrs={'placeholder': 'Mobile No'}),
			'secondary_school': TextInput(attrs={'placeholder': 'Secondary School'}),
			'secondary_percent': TextInput(attrs={'placeholder': 'Secondary Percentage'}),
			'senior_school': TextInput(attrs={'placeholder': 'Senior Secondary School'}),
			'senior_percent': TextInput(attrs={'placeholder': 'Senior Secondary Percentage'}),
			'College_name': TextInput(attrs={'placeholder': 'College Name'}),
			'Stream': TextInput(attrs={'placeholder': 'Branch'}),
			'Graduation_percent': TextInput(attrs={'placeholder': 'Graduation Percent'}),
			'Skills': TextInput(attrs={'placeholder': 'Skills'}),
			'exp_1': TextInput(attrs={'placeholder': 'Training organization'}),
			'exp_1_about': TextInput(attrs={'placeholder': 'Project'}),
		}
		exclude=('Id',)  

class PostForm(ModelForm):

	class Meta:
		model=posts
		widgets = {
			'Post_name': TextInput(attrs={'placeholder': 'Post Name'}),
			'Stream': TextInput(attrs={'placeholder': 'Stream'}),
			'Percent_Criteria': TextInput(attrs={'placeholder': 'Percentage'}),
			'Salary': TextInput(attrs={'placeholder': 'Salary'}),
			'Experience': TextInput(attrs={'placeholder': 'Experience'}),
			'Vacancy': TextInput(attrs={'placeholder': 'Vacancy'}),
			'Deadline': TextInput(attrs={'placeholder': 'Deadline Date'}),
		}
		exclude=('recruiter_id',)


				  
class AcceptForm(ModelForm):
	class Meta:
		model=Users_Apply
		exclude=('Seekerid','Companyid','Postid','Apply',)

	
