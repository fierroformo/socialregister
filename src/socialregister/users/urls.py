# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from socialregister.users import views


urlpatterns = patterns(
    '',
    url(
        r'^activate/(?P<activation_code>\w+)$',
        views.UserActivation.as_view()
    ),
    url(
        r"^activation-message/$",
        views.UserActivationMessage.as_view(),
        name="activation_message"
    ),
    url(
        r"^activation-successful/$",
        views.UserActivationSuccessful.as_view(),
        name="activation_successful"
    ),
    url(
        r"^complete-data/$",
        views.UserCompleteData.as_view(),
        name="complete_data"
    ),
    url(
        r"^delete/connection/(?P<provider>[\w\-]+)/$",
        views.UserDeleteConnection.as_view(),
        name="delete_connection"
    ),
    url(r"^login/$", views.UserLogin.as_view(), name="login"),
    url(r"^logout/$", views.user_logout, name="logout"),
    url(
        r"^set-password/$",
        views.UserSetPassword.as_view(),
        name="set_password"
    ),
    url(r"^register/$", views.UserRegister.as_view(), name="register"),
    url(
        r"^unset-password/$",
        views.UserUnsetPassword.as_view(),
        name="unset_password"
    ),
)
