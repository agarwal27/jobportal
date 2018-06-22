from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import myUser
from django.template import loader
#from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView,DeleteView
from .models import recruitersdetail,seekersdetails,posts,Users_Apply
from .forms import CompanyForm,UserForm,PostForm,AcceptForm

def index(request):
	return render(request,"register/index.html")

def recruitersdash(request):
    company=recruitersdetail.objects.filter(recruiter_id=request.session['seeker_id'])
    template=loader.get_template('register/recruitersdashboard.html')
    context ={'company': company}
    return HttpResponse(template.render(context, request))

def applicants(request):
    queryset=recruitersdetail.objects.filter(recruiter_id=request.session['seeker_id'])
    queryset1=Users_Apply.objects.all()
    template=loader.get_template('register/applicants.html')
    context ={'queryset': queryset,'queryset1': queryset1}
    return HttpResponse(template.render(context, request))

def seekersdash(request):
    queryset=seekersdetails.objects.filter(Id=request.session['seeker_id'])
    queryset1=posts.objects.all()
    queryset2=Users_Apply.objects.all()
    queryset3=recruitersdetail.objects.all()
    # queryset4 = queryset1 | queryset3  # merge querysets
    # queryset=seekersdetails.query.join(recruitersdetail, promote=True)
    context ={'queryset': queryset, 'queryset1': queryset1, 'queryset2': queryset2,'queryset3': queryset3,}
    return render(request,"register/seekerdashboard.html",context)  

def myprofile(request):
    queryset=seekersdetails.objects.filter(Id=request.session['seeker_id'])
    context ={'queryset': queryset}
    return render(request,"register/myprofile.html",context)

def notifications(request):
    queryset=seekersdetails.objects.filter(Id=request.session['seeker_id'])
    queryset1=Users_Apply.objects.all()
    context ={'queryset': queryset, 'queryset1': queryset1,}
    return render(request,"register/mynotifications.html",context)


def apply(request,post_id):
    if request.method == "POST":

        form = AcceptForm(request.POST)
        if form.is_valid():
            
            queryset2 = posts.objects.get(pk=post_id)
            queryset = seekersdetails.objects.get(Id=request.session['seeker_id'])
            queryset1 = recruitersdetail.objects.get(recruiter_id=queryset2.recruiter_id)

            instance3 = form.save(commit=False)

            instance3.Seekerid = queryset
            instance3.Companyid = queryset1
            instance3.Postid = queryset2
            instance3.Apply = 0

            instance3.save()
            return redirect('register:dashseeker') 
           
        else:

            
            return HttpResponse("notsuccess") 
    else:
        form = AcceptForm()
    return render(request, 'register/apply.html', {'form': form})
           


def accept(request,apply_id):

    if request.method == "POST":

        form = AcceptForm(request.POST)
        if form.is_valid():
            print(apply_id)
            print("abc")
            instance3=Users_Apply.objects.get(pk=apply_id)
            
            instance3.Apply=1
            #instance=Users_Apply.objects.all()

            instance3.save()
            
            return redirect('register:dashrecruit')  
           
        else:

            
            return HttpResponse("notsuccess") 
    else:
        form = AcceptForm()
    return render(request, 'register/accept.html', {'form': form})

def post(request):
    if request.method == "POST":

        form = PostForm(request.POST)
        if form.is_valid():
            instance=myUser.objects.get(pk=request.session['seeker_id'])
            company = form.save(commit=False)
            company.recruiter_id = instance
            company.save()
            
            return redirect('register:dashrecruit')  
           
        else:

            
            return HttpResponse("notsuccess") 
    else:
        form = PostForm()
    return render(request, 'register/post_reg.html', {'form': form})
    

def register(request):
    
    if request.method == "POST":

        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            instance=myUser.objects.get(pk=request.session['seeker_id'])

            employee = form.save(commit=False)
            employee.Id = instance
            employee.save()
            instance.status=1
            print(instance)
            instance.save()
            # return HttpResponse(employee.Id) 
            
            return redirect('register:dashseeker')
           
        else:

            
            return HttpResponse("notsuccess") 
    else:
        form = UserForm()
    return render(request, 'register/emp_reg.html', {'form': form})





def login(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            instance=myUser.objects.get(pk=request.session['seeker_id'])
            
            company = form.save(commit=False)
            company.recruiter_id = instance
            # post.published_date = timezone.now()
            company.save()
            instance.status=1
            print(instance)
            instance.save()
            # return redirect('post_detail', pk=post.pk)
            return redirect('register:dashrecruit') 
        else:
            return HttpResponse("notsuccess")

    else:
        form = CompanyForm()
    return render(request, 'register/comp_reg.html', {'form': form})

def profile_update(request,recruiter_id):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            instance1=myUser.objects.get(pk=request.session['seeker_id'])
            
            company = form.save(commit=False)
            company.recruiter_id = instance1
            a=recruitersdetail.objects.get(pk=recruiter_id)
            form=CompanyForm(request.POST, request.FILES,instance=a)
            form.save()
        
            return redirect('register:dashrecruit') 
        else:
            return HttpResponse("notsuccess")

    else:
        a=recruitersdetail.objects.get(pk=recruiter_id)
        form = CompanyForm(instance=a)
    return render(request, 'register/comp_reg.html', {'form': form})

def profile1_update(request,seeker1_id):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            instance1=myUser.objects.get(pk=request.session['seeker_id'])
            
            company = form.save(commit=False)
            company.Id = instance1
            a=seekersdetails.objects.get(pk=seeker1_id)
            form=UserForm(request.POST, request.FILES,instance=a)
            form.save()
        
            return redirect('register:dashseeker') 
        else:
            return HttpResponse("notsuccess")

    else:
        a=seekersdetails.objects.get(pk=seeker1_id)
        form = UserForm(instance=a)
    return render(request, 'register/emp_reg.html', {'form': form})

def all_posts(request):
    queryset=recruitersdetail.objects.filter(recruiter_id=request.session['seeker_id'])
    queryset1=posts.objects.all()
    template=loader.get_template('register/view_posts.html')
    context ={'queryset': queryset,'queryset1': queryset1}
    return HttpResponse(template.render(context, request))

def post_update(request,post_id):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance1=myUser.objects.get(pk=request.session['seeker_id'])
            
            company = form.save(commit=False)
            company.recruiter_id = instance1
            a=posts.objects.get(pk=post_id)
            form=PostForm(request.POST, request.FILES,instance=a)
            form.save()
        
            return redirect('register:dashrecruit') 
        else:
            return HttpResponse("notsuccess")

    else:
        a=posts.objects.get(pk=post_id)
        form = PostForm(instance=a)
    return render(request, 'register/post_reg.html', {'form': form})

def post_delete(request,post_id):
     posts.objects.filter(pk=post_id).delete()
     return render(request,"register/view_posts.html")

def delete_account(request):
    print("abc")
    myUser.objects.filter(pk=request.session['seeker_id']).delete()
    return redirect('home') 

def view_profile(request,profile_id):
    company=recruitersdetail.objects.filter(pk=profile_id)
    template=loader.get_template('register/rec_profile.html')
    context ={'company': company}
    return HttpResponse(template.render(context, request))

def view_profile1(request,profile_id):
    queryset=seekersdetails.objects.filter(pk=profile_id)
    template=loader.get_template('register/sec_profile.html')
    context ={'queryset': queryset}
    return HttpResponse(template.render(context, request))

def reject(request,apply_id):
    Users_Apply.objects.filter(pk=apply_id).delete()
    return redirect('register:dashrecruit') 
