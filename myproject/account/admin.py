from django.contrib import admin
from .models import UserProfile, PostDetail, CommentDetail

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(PostDetail)
admin.site.register(CommentDetail)