# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


BACKENDS = {
    'facebook': {
        'api_key_config': getattr(settings, "SOCIAL_AUTH_FACEBOOK_KEY", None),
        'description': '''
            * Crea la aplicación:
              https://developers.facebook.com/quickstarts/?platform=web
            * Agregar 'social.backends.facebook.FacebookOAuth2' a la tupla
              AUTHENTICATION_BACKENDS
            * SOCIAL_AUTH_FACEBOOK_KEY = '<key>'
            * SOCIAL_AUTH_FACEBOOK_SECRET = '<secret>'
            * SOCIAL_AUTH_FACEBOOK_SCOPE = [<scope>]
        ''',
        'title': 'Facebook'
    },
    'twitter': {
        'api_key_config': getattr(settings, "SOCIAL_AUTH_TWITTER_KEY", None),
        'description': '''
            * Crea la aplicación: https://apps.twitter.com/
            * Agregar 'social.backends.twitter.TwitterOAuth' a la tupla
              AUTHENTICATION_BACKENDS
            * SOCIAL_AUTH_TWITTER_KEY = '<key>'
            * SOCIAL_AUTH_TWITTER_SECRET = '<secret>'
        ''',
        'title': 'Twitter'
    },
    'google-oauth2': {
        'api_key_config': getattr(
            settings, "SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", None
        ),
        'description': '''
            * Crea la aplicación: https://console.developers.google.com/project
            * Agregar 'social.backends.google.GoogleOAuth2' a la tupla
              AUTHENTICATION_BACKENDS
            * SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<key>'
            * SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<secret>'
        ''',
        'title': 'Google+'
    },
    'live': {
        'api_key_config': getattr(settings, "SOCIAL_AUTH_LIVE_KEY", None),
        'description': '''
            * Crea la aplicación:
              https://account.live.com/developers/applications/
            * Agregar 'social.backends.live.LiveOAuth2' a la tupla
              AUTHENTICATION_BACKENDS
            * SOCIAL_AUTH_LIVE_KEY = '<key>'
            * SOCIAL_AUTH_LIVE_SECRET = '<secret>'
        ''',
        'title': 'Outlook'
    },
    'github': {
        'api_key_config': getattr(settings, "SOCIAL_AUTH_GITHUB_KEY", None),
        'description': '''
            * Crea la aplicación: https://github.com/settings/applications
            * Agregar 'social.backends.github.GithubOAuth2' a la tupla
              AUTHENTICATION_BACKENDS
            * SOCIAL_AUTH_GITHUB_KEY = '<key>'
            * SOCIAL_AUTH_GITHUB_SECRET = '<secret>'
        ''',
        'title': 'Github'
    },
    'linkedin-oauth2': {
        'api_key_config': getattr(
            settings, "SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY", None
        ),
        'description': '''
            * Crea la aplicación: https://www.linkedin.com/secure/developer
            * Activar los permisos r_emailaddress y r_basicprofile al crear
              la aplicación
            * Agregar 'social.backends.linkedin.LinkedinOAuth2' a la tupla
              AUTHENTICATION_BACKENDS
            * SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = '<key>'
            * SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = '<secret>'
        ''',
        'title': 'Linkedin'
    }
}


class HomeView(TemplateView):
    template_name = 'home.html'
    backends = BACKENDS

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        connected = [
            backend.provider for backend in self.request.user.social_auth.all()
        ]
        for provider in self.backends:
            self.backends[provider]['connected'] = provider in connected

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
