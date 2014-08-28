# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from socialregister.users import views


urlpatterns = patterns('',
    url(r"^login/$", views.UserLogin.as_view(), name="login"),
    url(r"^logout/$", views.user_logout, name="logout"),
    url(r"^register/$", views.UserRegister.as_view(), name="register"),
)
