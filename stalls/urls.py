from django.conf.urls import url

from . import views

"""
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
"""
urlpatterns = [
    
    # ex: /stalls/5
    url(r'^(?P<stallId>\S+)$', views.detail, name='detail'),    
    # ex: /stalls
    url(r'^$', views.index, name='index'),
    


    # ex: /polls/5/results/
    #url(r'^(?P<stall_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<stall_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
