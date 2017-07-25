from django.conf.urls import url
from . import views
# from django.contrib import admin
app_name = 'friend'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add$', views.add, name = 'add'),
    url(r'^block$', views.block, name = 'block'),
    url(r'^list$', views.list, name = 'list'),
    url(r'^make_friend/(?P<id>\d+)$', views.make_friend, name = 'make_friend'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = 'remove'),
    url(r'^remove_block/(?P<id>\d+)$', views.remove_block, name = 'remove_block'),
    url(r'^make_block/(?P<id>\d+)$', views.make_block, name = 'make_block'),
    url(r'^profile/(?P<id>\d+)$', views.profile, name = 'profile'),
    # url(r'^info/(?P<id>\d+)$', views.info, name = 'info'),
    # url(r'^edit/(?P<id>\d+)$', views.edit, name = 'edit'),
    # url(r'^change/$', views.change, name = 'change'),

]
