# -*- coding: utf-8 -*-
from django.shortcuts import redirect
from social import exceptions as social_exceptions
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware


class AuthCanceledExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if isinstance(exception, social_exceptions.AuthCanceled):
            return redirect('users:login_canceled')

        return super(AuthCanceledExceptionMiddleware, self).process_exception(request, exception)
