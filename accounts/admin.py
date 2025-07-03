from django.contrib import admin
# from unfold.admin import ModelAdmin as UnfoldModelAdmin
from .models import User    

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'user_type', 'is_staff')
    search_fields = ('email', 'first_name', 'user_type')
    ordering = ('date_joined',)
    filter_horizontal = ('groups', 'user_permissions')
