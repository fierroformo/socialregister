from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import HomeView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^users/', include('socialregister.users.urls', namespace='users')),
)
