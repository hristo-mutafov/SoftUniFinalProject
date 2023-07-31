from django.contrib import admin
from django.contrib.auth.hashers import make_password

from Ecommerce.accounts.models import AppUser, UserProfile


@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    ordering = ('email',)

    list_display = ('email', 'is_active')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    search_fields = ('email',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('email', 'password')
        }),
        ('Additional Information', {
            'fields': ('is_active', 'is_staff', 'date_joined')
        }),
    )

    def add_view(self, request, form_url='', extra_context=None):
        if request.method == 'POST':
            form_class = self.get_form(request, obj=None)
            post_data = request.POST.copy()

            post_data['password'] = make_password(post_data['password'])
            form = form_class(post_data)

            if form.is_valid():
                app_user = form.save()

                return self.response_add(request, app_user)

        return super().add_view(request, form_url=form_url, extra_context=extra_context)


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    ordering = ('first_name', )

    list_display = ('__str__', 'first_name', 'city')
    list_filter = ('city', 'gender')
    search_fields = ('first_name', 'last_name', 'phone_number', 'address')

    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name', 'phone_number')
        }),
        ('Additional Information', {
            'fields': ('address', 'city', 'gender')
        }),
    )
