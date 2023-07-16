from django.contrib import admin

from Ecommerce.accounts.models import AppUser, UserProfile


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    pass
