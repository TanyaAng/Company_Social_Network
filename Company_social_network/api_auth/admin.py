from django.contrib import admin

from Company_social_network.api_auth.models import CompanyUser, Profile


@admin.register(CompanyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    ordering = ('is_active',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user')
