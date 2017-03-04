# -*- coding: utf-8 -*-
from django.contrib import messages
from django.shortcuts import redirect

from social import exceptions as social_exceptions
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware


class AuthCanceledExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, social_exceptions.AuthCanceled):
            messages.warning(request, "¡Cancelaste tu autenticación!")
            return redirect('users:login')

        return super(
            AuthCanceledExceptionMiddleware, self
        ).process_exception(request, exception)
