# -*- coding: utf-8 -*-
import hashlib
import random

from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_confirmation_email(activation_code, email):
    site = Site.objects.get_current()
    context = {
        'site': site,
        'activation_code': activation_code
    }
    subject = "Activa tu cuenta - %s" % site.domain
    email_text = render_to_string('email/activation.txt', context)
    email_html = render_to_string('email/activation.html', context)
    msg = EmailMultiAlternatives(
        subject, email_text, settings.DEFAULT_FROM_EMAIL, [email]
    )
    msg.attach_alternative(email_html, 'text/html')
    msg.send()


def generate_activation_code(email):
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    if isinstance(email, unicode):
        email = email.encode('utf-8')
    return hashlib.sha1(salt + email).hexdigest()
