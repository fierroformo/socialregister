# -*- coding: utf-8 -*-
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import logout
from django.shortcuts import redirect
from django.views.generic.edit import FormView

from socialregister.users.forms import RegisterForm


class UserLogin(FormView):
    form_class = AuthenticationForm
    template_name = "users/form.html"

    def form_valid(self, form):
        login(self.request, form.get_user())
        return redirect("/")

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('home')
        return super(UserLogin, self).dispatch(*args, **kwargs)


def user_logout(request):
    return logout(request, next_page="users:login")


class UserRegister(FormView):
    form_class = RegisterForm
    success_url = '/'
    template_name = "users/register.html"

    def form_valid(self, form):
        u = form.save()
        u.username = u.email
        u.set_password(form.cleaned_data['password'])
        u.save()
        return redirect("users:login")

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('home')
        return super(UserRegister, self).dispatch(*args, **kwargs)
