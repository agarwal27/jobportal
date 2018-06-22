"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views import generic
from django.conf.urls import url
from django.urls import include,path
from accounts.views import login_view,register_view,logout_view,home_view
from register.views import recruitersdash,seekersdash,applicants,post,myprofile,notifications,all_posts
from django.conf.urls.static import static

urlpatterns = [
   
    path('admin/', admin.site.urls),
    
    path('register/',include('register.urls', namespace='register')),
    path('home/',home_view,name='home'),
    path('logins/',login_view,name='logins'),
    path('registration/',register_view,name='registration'),
    path('logout/',logout_view,name='logout'),
    path('applicants/',applicants,name='applicants'),
    path('add_post/',post,name='add_post'),
    path('all_posts/',all_posts,name='all_posts'),
    path('myprofile/',myprofile,name='myprofile'),
    path('mynotifications/',notifications,name='notifications'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)