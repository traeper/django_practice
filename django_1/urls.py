from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^app1/', include('app1.urls')),
    url(r'^admin/', admin.site.urls),
]
