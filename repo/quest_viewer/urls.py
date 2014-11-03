from django.conf.urls import patterns, url

from quest_viewer import views

urlpatterns = patterns('',
		    url(r'^$', views.index, name='index'),
		    url(r'^discipline/(?P<discipline_id>\d+)$', views.discipline, name='discipline'),
		    )
