from django.conf.urls import url
from . import views

urlpatterns = [
    url('pessoas/', views.PessoasListar.as_view()),
    url('pessoa/(?P<pk>[0-9]+)/$', views.PessoaDetalhes.as_view())
]