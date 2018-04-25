from django.conf.urls import url
from . import views

app_name = 'words'

urlpatterns = [
    url(r'^detail/(?P<pk>[0-9]+)$', views.AbbreviationDetailView.as_view(),
        name='abbreviation_detail'),
    url(r'^create/$', views.AbbreviationCreate.as_view(),
        name='abbreviation_create'),
    url(r'^edit/(?P<pk>[0-9]+)$', views.AbbreviationUpdate.as_view(),
        name='abbreviation_edit'),
    url(r'^delete/(?P<pk>[0-9]+)$', views.AbbreviationDelete.as_view(),
        name='abbreviation_delete'),
]
