from django.conf.urls import * 
from rest_framework.urlpatterns import format_suffix_patterns
from demo_app import views
from demo_app.views import MazeList, RoomList, MazeDetail, RoomDetail

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('my_demo.views',
    # Examples:
    # url(r'^$', 'my_demo.views.home', name='home'),
    # url(r'^my_demo/', include('my_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^rooms/(?P<room_id>\d+)/$', views.room, name='room'),
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    url(r'^api/', views.api_root),
    url(r'^r_mazes/$', MazeList.as_view(), name='maze-list'),
    url(r'^r_mazes/(?P<pk>\d+)/$', MazeDetail.as_view(), name='maze-detail'),
    url(r'^r_rooms/$', RoomList.as_view(), name='room-list'),
    url(r'^r_rooms/(?P<pk>\d+)/$', RoomDetail.as_view(), name='room-detail'),
    url(r'^mazes/', views.index),

    
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

