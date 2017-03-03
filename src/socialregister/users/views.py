# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import get_user_model, login

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import logout
from django.shortcuts import get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from django.views.generic.edit import FormView

from socialregister.users.forms import (
    CompleteDataForm, RegisterForm, SetPasswordForm
)
from socialregister.users.mixins import AuthenticationMixin
from socialregister.users.utils import (
    generate_activation_code, send_confirmation_email
)
from socialregister.views import BACKENDS


class UserActivation(View):

    def get(self, request, **kwargs):
        UserModel = get_user_model()
        user = get_object_or_404(
            UserModel, activation_code=kwargs['activation_code'],
            is_active=True)
        user.is_active = True
        user.save()
        return redirect('users:activation_successful')


class UserActivationMessage(AuthenticationMixin, TemplateView):
    template_name = 'users/activation_message.html'


class UserActivationSuccessful(AuthenticationMixin, TemplateView):
    template_name = 'users/activation_successful.html'


class UserCompleteData(FormView):
    form_class = CompleteDataForm
    template_name = "users/complete_data.html"

    def form_valid(self, form):
        email = form.data['email']
        self.request.user.email = email
        self.request.user.username = email
        self.request.user.save()
        return redirect('/')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        if self.request.user.email:
            return redirect('/')
        return super(UserCompleteData, self).dispatch(*args, **kwargs)


class UserUnsetPassword(View):

    def post(self, *args, **kwargs):
        self.request.user.set_unusable_password()
        self.request.user.save()

        if not self.request.user.social_auth.count():
            return redirect('users:set_password')

        return redirect('/')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserUnsetPassword, self).dispatch(*args, **kwargs)


class UserDeleteConnection(View):

    def post(self, *args, **kwargs):
        self.request.user.social_auth.get(
            user_id=self.request.user.id, provider=kwargs['provider']).delete()

        if not self.request.user.social_auth.count() and \
           not self.request.user.has_usable_password():
            return redirect('users:set_password')

        return redirect('/')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserDeleteConnection, self).dispatch(*args, **kwargs)


class UserLogin(AuthenticationMixin, FormView):
    form_class = AuthenticationForm
    template_name = "users/login.html"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect("/")

    def get_context_data(self, queryset=None, **kwargs):
        context = super(UserLogin, self).get_context_data(**kwargs)
        context['backends'] = BACKENDS
        return context


def user_logout(request):
    return logout(request, next_page="users:login")


class UserRegister(AuthenticationMixin, FormView):
    form_class = RegisterForm
    success_url = '/'
    template_name = "users/register.html"

    def form_valid(self, form):
        u = form.save()
        u.username = u.email
        u.set_password(form.cleaned_data['password'])
        u.is_active = settings.DEBUG
        u.activation_code = generate_activation_code(u.email)
        u.save()
        send_confirmation_email(u.activation_code, u.email)
        return redirect("users:activation_message")


class UserSetPassword(FormView):
    form_class = SetPasswordForm
    template_name = "users/set_password.html"

    def form_valid(self, form):
        self.request.user.set_password(form.cleaned_data['password'])
        self.request.user.save()
        return redirect("/")

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(UserSetPassword, self).dispatch(*args, **kwargs)
