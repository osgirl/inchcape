from django.conf.urls import url

from .views import index


app_name = 'medrecord'
urlpatterns = [
    url(r'^$', index, name='totp'),
]
