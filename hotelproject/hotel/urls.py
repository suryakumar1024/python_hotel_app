from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # url(r'^hotel/', TemplateView.as_view(template_name='index.html')),
    url(r'^$', views.index, name='index'),
    url(r'^menu/$', views.menu_details, name='menu'),
    url(r'^view/$', views.view_hotel, name='view'),
    url(r'^(?P<hotel_id>[0-9]+)$', views.detail, name='check'),
]