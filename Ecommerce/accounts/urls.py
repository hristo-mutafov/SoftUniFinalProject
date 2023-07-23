from django.contrib.auth.views import LogoutView
from django.urls import path, include

from Ecommerce.accounts.views import *

urlpatterns = (
    path('auth/', include([
        path('login/', Login.as_view(), name='login'),
        path('register/', Register.as_view(), name='register'),
        path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    ])),

    path('profile/', include([
        path('', show_navigator, name='profile_navigator'),
        path('settings/', show_profile_settings, name='profile_settings'),
        path('delete/', DeleteProfile.as_view(), name='delete_profile'),
        path('update_name/', update_user_name),
        path('update_email/', update_user_email),
        path('change_password/', update_user_password),

        path('addresses/', show_profile_address_information, name='profile_addresses'),
        path('update_city/', update_user_city),
        path('update_address/', update_user_address),
        path('update_phone_number/', update_user_phone_number),
    ]))
)
