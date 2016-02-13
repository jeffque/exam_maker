from django.conf.urls import include, url
from django.contrib import admin
import quest_viewer

urlpatterns = [
    # Examples:
    # url(r'^$', 'repo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^v/', include('quest_viewer.urls', namespace='quest_viewer')),
]
