from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<initial>[-\w]+)/$', views.index, name='index_by_letter'),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name="detail"),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.edit, name='edit'),
]