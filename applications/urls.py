from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^requesters/(?P<user_id>[0-9]+)/', include([
        url(r'^$', views.requester_dashboard, name='requester-dashboard'),
        url(r'^createapplication$', views.create_application, name='create-application')
    ])),
     url(r'^supervisors/(?P<user_id>[0-9]+)/', include([
        url(r'^$', views.supervisor_dashboard, name='supervisor-dashboard'),
        url(r'makerecomendation/(?P<app_id>[0-9]+)$', views.make_recommendation, name='make-recommendation'),
    ]))
]
