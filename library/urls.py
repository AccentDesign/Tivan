from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^welcome/$', views.welcome, name='registration_welcome'),
    url(r'^connection/$', views.connection, name='registration_connection'),
    url(r'^library/$', views.library, name="library"),
    url(r'^library/(?P<initial>[-\w]+)/$', views.library, name="library_by_letter"),
    url(r'^your-collection/$', views.collection, name="your_collection"),
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name="detail"),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.edit, name="edit"),
    url(r'^profile/edit/', views.edit_profile, name='edit_profile'),
]