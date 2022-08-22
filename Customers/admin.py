from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User


class CustomerAdmin(BaseUserAdmin):
    list_display = ['full_name', 'email', 'phone_number']
    list_filter = ('is_admin',)
    fieldsets = (
        ('Main', {'fields': ('full_name', 'email', 'phone_number', 'password')}),
        ('Personal info', {'fields': ('is_active',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('full_name', 'phone_number', 'email', 'password1', 'password2')
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomerAdmin)
admin.site.unregister(Group)
