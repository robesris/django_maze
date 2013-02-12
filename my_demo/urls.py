from django.conf.urls import * 
from demo_app import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_demo.views.home', name='home'),
    # url(r'^my_demo/', include('my_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^rooms/(?P<room_id>\d+)/$', views.room, name='room'),
    #url(r'^mazes/', views.maze),

)
