from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^requesters/(?P<userid>[0-9]+)/', include([
        url(r'^$', views.requester_dashboard, name='requester-dashboard'),
        url(r'^createapplication$', views.create_application, name='create-application')
    ])),
     url(r'^supervisors/(?P<userid>[0-9]+)/', include([
        url(r'^$', views.supervisor_dashboard, name='supervisor-dashboard'),
    ]))
]