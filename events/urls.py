from django.conf.urls import url
from . import views

urlpatterns = [
                url(r'^updatestatus/(?P<eid>\S+)$', views.updateStatus, name='updateStatus'),
                url(r'^(?P<eid>\S+)$', views.detail, name='detail'),                
                url(r'^$', views.index, name = 'index'),
              ]        
