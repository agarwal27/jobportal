from django.contrib import admin

# Register your models here.
from .models import seekersdetails,posts,recruitersdetail,Users_Apply
admin.site.register(seekersdetails)
admin.site.register(posts)
admin.site.register(recruitersdetail)
admin.site.register(Users_Apply)