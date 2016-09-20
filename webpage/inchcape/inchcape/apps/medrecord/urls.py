from django.conf.urls import url

from .views import index, med_record


app_name = 'medrecord'
urlpatterns = [
    url(r'^$', index, name='totp'),
    # url(r'^med-record/$', med_record, name='med-record'),
]
