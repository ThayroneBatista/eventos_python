from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url('eventos/$', views.EventosListar.as_view()),
    url('evento/(?P<pk>[0-9]+)/$', views.EventoDetalhes.as_view()),
    url('eventos_entre/$', views.EventosIntervalo.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)