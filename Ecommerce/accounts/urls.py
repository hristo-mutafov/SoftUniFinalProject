from django.urls import path, include

from Ecommerce.accounts.views import Login, Register, show_navigator

urlpatterns = (
    path('auth/', include([
        path('login/', Login.as_view(), name='login'),
        path('register/', Register.as_view(), name='register')
    ])),

    path('profile/', include([
        path('', show_navigator, name='profile_navigator'),
    ]))
)
