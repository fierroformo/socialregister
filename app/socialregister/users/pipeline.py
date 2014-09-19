# -*- coding: utf-8 -*-
from socialregister.users.models import User


def create_user(strategy, details, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    if strategy.backend.name == 'twitter' and not details['email']:
        username = details['username'] + '@twitter.com'
    elif strategy.backend.name == 'linkedin-oauth2' and not details['email']:
        username = details['username']
    else:
        username = details['email']

    user = User.objects.get_or_create(
        username=username,
        defaults={
            'email': details['email'], 'first_name': details['first_name'],
            'last_name': details['last_name'], 'is_active': True})[0]

    return {
        'is_new': True,
        'user': user
    }
