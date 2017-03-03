# -*- coding: utf-8 -*-
from django.shortcuts import redirect


class AuthenticationMixin(object):

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect('/')
        return super(AuthenticationMixin, self).dispatch(*args, **kwargs)
