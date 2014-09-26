# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home.html'
    backends = settings.BACKENDS

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        for key, value in self.backends.items():
            self.backends[key]['connected'] = False

        for backend in self.request.user.social_auth.all():
            self.backends[backend.provider]['connected'] = True

        context['backends'] = self.backends
        return context

    @method_decorator(login_required(login_url='/users/login'))
    def dispatch(self, *args, **kwargs):
        if not self.request.user.email:
            return redirect('users:complete_data')

        if not self.request.user.social_auth.count() and \
           not self.request.user.has_usable_password():
            return redirect('users:set_password')

        return super(HomeView, self).dispatch(*args, **kwargs)
