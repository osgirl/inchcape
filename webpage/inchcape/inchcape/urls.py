from django.conf.urls import include, url
from django.contrib import admin
# from django.contrib.auth import views as auth_views

from .views import IndexView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('medrecord.urls')),
    # url(r'^accounts/', include('allauth.urls')),
    # url(r'^logout/$', auth_views.logout,
        # name='logout', kwargs={'next_page': '/'})
]
