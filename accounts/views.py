from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login,logout,get_user_model
# Create your views here.
from .forms import userloginform,UserRegisterForm
from .models import myUser

def home_view(request):
	return render(request,"accounts/front.html")

def login_view(request):
	
	if request.method == "POST":
		form = userloginform(request.POST)
		if form.is_valid():
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('password')
			user=authenticate(request,username=username,password=password)
			if user is not None:
        
				request.session['seeker_id'] = user.id

				request.session['status'] = user.user_types

				

				if request.session['status'] =='recruiters':
					if user.status==0:

						return redirect('register:login')
					else:
						return redirect('register:dashrecruit')	
					
				else:
					if user.status==0:	

						return redirect('register:register')
					else:
						return redirect('register:dashseeker')
			else:
				return HttpResponse('hii')
	else:
		form=userloginform()
	return render(request,"accounts/log.html",{'form':form})

def register_view(request):
	form=UserRegisterForm(request.POST or None)
	if form.is_valid():
		user=form.save(commit=False)
		password=form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user=authenticate(username=user.username,password=password)
		if new_user is not None:
        
				
			return redirect('home')
		else:
			return HttpResponse('hello')

	return render(request,"accounts/register.html",{'form':form})	
def logout_view(request):
	del request.session['seeker_id']
	return redirect('home')	