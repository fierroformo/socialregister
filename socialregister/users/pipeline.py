from socialregister.users.models import User


def create_user(strategy, details, user=None, *args, **kwargs):
    if user:
        return {'is_new': False}

    user = User.objects.get_or_create(
        email=details['email'],
        defaults={
            'username': details['email'], 'first_name': details['first_name'],
            'last_name': details['last_name'], 'is_active': True})[0]

    return {
        'is_new': True,
        'user': user
    }
