import json

from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
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


@login_required()
def show_navigator(request):
    return render(request, 'profile/profile.html')


@login_required
def show_profile_settings(request):
    user = request.user
    context = {
        'name': f'{user.userprofile.first_name} {user.userprofile.last_name}',
        'email': user.email
    }

    return render(request, 'profile/profile_settings.html', context)


def update_user_name(request):
    if request.method == 'POST':
        try:
            user = request.user
            raw_data = request.body
            data = json.loads(raw_data)

            if not data['first_name'].strip() or not data['last_name'].strip():
                return JsonResponse({'message': 'Fill the fields!'}, status=400)

            user.userprofile.first_name = data['first_name']
            user.userprofile.last_name = data['last_name']
            user.userprofile.save()
            return JsonResponse({'message': 'Changes applied successfully!'}, status=200)

        except:
            return JsonResponse({'message': 'Something went wrong'}, status=500)

    else:
        raise Http404()


def update_user_email(request):
    if request.method == 'POST':
        try:
            user = request.user
            raw_data = request.body
            data = json.loads(raw_data)

            if not data['email'].strip() or not data['password'].strip():
                return JsonResponse({'message': 'Fill the fields!'}, status=400)

            if data['email'] == user.email:
                return JsonResponse({'message': 'Current email entered!'}, status=400)

            if not user.check_password(data['password']):
                return JsonResponse({'message': 'Wrong password!'}, status=400)

            user.email = data['email']
            user.save()

            return JsonResponse({'message': 'Changes applied successfully!'}, status=200)

        except:
            return JsonResponse({'message': 'Something went wrong'}, status=500)

    else:
        raise Http404()


def update_user_password(request):
    if request.method == 'POST':
        try:
            user = request.user
            raw_data = request.body
            data = json.loads(raw_data)

            if not data['old_password'].strip() or\
                    not data['new_password'].strip() or\
                    not data['repeat_new_password'].strip():

                return JsonResponse({'message': 'Fill the fields!'}, status=400)

            if not user.check_password(data['old_password']):
                return JsonResponse({'message': 'Wrong old password!'}, status=400)

            if data['new_password'] != data['repeat_new_password']:
                return JsonResponse({'message': 'The passwords do not match!'}, status=400)

            validate_password(data['new_password'])

            user.set_password(data['new_password'])
            user.save()

            return JsonResponse({'message': 'Changes applied successfully!'}, status=200)

        except ValidationError:
            return JsonResponse({'message': 'Password is too weak!'}, status=400)
        except KeyError:
            return JsonResponse({'message': 'Something went wrong'}, status=500)

    else:
        raise Http404()


class DeleteProfile(LoginRequiredMixin, views.View):
    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile = user.userprofile

        user.delete()
        profile.delete()

        return redirect('index')
