from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', admin.site.urls),
    url(r'^', include('eventos_app.urls')),
    url(r'^', include('pessoas_app.urls'))
]