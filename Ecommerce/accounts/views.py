from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from Ecommerce.accounts.forms import LoginForm, RegisterForm
from Ecommerce.accounts.models import UserProfile

UserModel = get_user_model()


class Login(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        if next_url:
            return next_url
        return reverse_lazy('index')


class Register(views.CreateView):
    model = UserModel
    template_name = 'auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        data = super().form_valid(form)

        user_profile = UserProfile(user=self.object)
        user_profile.save()

        login(self.request, self.object)
        return data


def show_navigator(request):
    return render(request, 'profile/profile.html')