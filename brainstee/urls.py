from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^profiles/(\d+)',views.profiles,name='profiles'),
    url(r'^seek/',views.seek,name = 'seek'),
    url(r'^helpout/',views.helpout,name = 'helpout'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
 ]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
