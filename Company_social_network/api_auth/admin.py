from django.contrib import admin

from Company_social_network.api_auth.models import CompanyUser, Profile


@admin.register(CompanyUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
