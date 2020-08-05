from django.contrib import admin

# Register your models here.
from .models import Profile

# admin.site.register(User)

# class UserAdmin(admin.ModelAdmin): #define admin class
#     list_display = ('hp_no', 'name', 'email', 'is_admin', 'created_at', 'updated_at')
# admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    model = Profile

admin.site.register(Profile, ProfileAdmin)

# class CaseAdmin(admin.ModelAdmin):
#     list_display = ('address', 'time', 'description', 'case_type', 'id_required', 'updated_at')
# admin.site.register(Case, CaseAdmin)

# class ResponseAdmin(admin.ModelAdmin):
#     list_display = ('user', 'case', 'response', 'arrival_time')
# admin.site.register(Response, ResponseAdmin)

# class GroupAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'created_at', 'updated_at', 'display_members')
# admin.site.register(Group, GroupAdmin)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'user', 'image', 'no_votes', 'created_at', 'updated_at')
# admin.site.register(Post, PostAdmin)

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('content', 'post', 'user', 'created_at')
# admin.site.register(Comment, CommentAdmin)
