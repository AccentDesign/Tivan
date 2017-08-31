from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^welcome/$', views.welcome, name='registration_welcome'),
    url(r'^connection/$', views.connection, name='registration_connection'),
    url(r'^library/$', views.library, name="library"),
    url(r'^library/(?P<initial>[-\w]+)/$', views.library, name="library_by_letter"),
    url(r'^your-collection/$', views.collection, name="your_collection"),
    url(r'^(?P<slug>[-\w]+)/$', views.media_item_detail, name="media_item_detail"),
    url(r'^(?P<slug>[-\w]+)/edit/$', views.media_item_edit, name="media_item_edit"),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.media_item_delete, name="media_item_delete"),
    url(r'^profile/edit/', views.profile_edit, name='edit_profile'),
]