from django.conf.urls import url
from django.urls import path
from . import views
from .views import recruitersdash,seekersdash
app_name='register'
#app_name="register"

urlpatterns = [
path('index/',views.index,name='index'),
path('login/',views.login,name='login'),
path('register/',views.register,name='register'),
path('dashr/',recruitersdash,name='dashrecruit'),
path('dashs/',seekersdash,name='dashseeker'),
url(r'^(?P<post_id>[0-9]+)/$',views.apply, name='detail1'),
url(r'^accept/(?P<apply_id>[0-9]+)/$',views.accept, name='detail'),
url(r'^reject/(?P<apply_id>[0-9]+)/$',views.reject, name='reject'),
url(r'^profile_update/(?P<recruiter_id>[0-9]+)/$',views.profile_update,name='profile_update'),
url(r'^profile1_update/(?P<seeker1_id>[0-9]+)/$',views.profile1_update,name='profile1_update'),
url(r'^post_update/(?P<post_id>[0-9]+)/$',views.post_update,name='post_update'),
url(r'^post_delete/(?P<post_id>[0-9]+)/$',views.post_delete,name='post_delete'),
url(r'^delete_account/$',views.delete_account,name='delete_account'),
url(r'^delete_account1/$',views.delete_account,name='delete_account'),
url(r'^view_profile/(?P<profile_id>[0-9]+)/$',views.view_profile,name='view_profile'),
url(r'^view_profile1/(?P<profile_id>[0-9]+)/$',views.view_profile1,name='view_profile1'),
#url(r'^post/(?P<apply_id>[0-9]+)/$',views.PostUpdate.as_view, name='post-update'),
#url(r'^post/(?P<apply_id>[0-9]+)/delete/$',views.AlbumDelete.as_view, name='post-delete'),
]