"""
app1/urls.py
"""

from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^do_job', views.api_do_job, name='api_do_job'),
]
