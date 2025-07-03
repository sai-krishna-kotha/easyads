from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from unfold.admin import ModelAdmin as UnfoldModelAdmin
from .models import User    
# from django.utils.translation import gettext_lazy as _

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name',)}),
    #     (_('Permissions'), {
    #         'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    #     (_('Role Info'), {'fields': ('user_type',)}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'first_name', 'user_type', 'password1', 'password2'),
    #     }),
    # )
    list_display = ('email', 'first_name', 'user_type', 'is_staff')
    search_fields = ('email', 'first_name', 'user_type')
    ordering = ('date_joined',)

    # Tell Django to use email as the login field
    filter_horizontal = ('groups', 'user_permissions')
