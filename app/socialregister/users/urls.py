# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from socialregister.users import views


urlpatterns = patterns('',
    url(r"^complete-data/$", views.UserCompleteData.as_view(), name="complete_data"),
    url(r"^delete/conection/(?P<provider>[\w\-]+)/$", views.UserDeleteConection.as_view(), name="delete_conection"),
    url(r"^login/$", views.UserLogin.as_view(), name="login"),
    url(r"^logout/$", views.user_logout, name="logout"),
    url(r"^set-password/$", views.UserSetPassword.as_view(), name="set_password"),
    url(r"^register/$", views.UserRegister.as_view(), name="register"),
    url(r"^unset-password/$", views.UserUnsetPassword.as_view(), name="unset_password"),
)
