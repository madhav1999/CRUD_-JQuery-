from django.urls import path, re_path
from . import views

urlpatterns = [
    path("details/insert", views.first, name='insertv'),
    path("details/", views.listview, name='listv'),
    re_path(r'^details/(?P<id>[0-9]+)/$', views.detailsview, name='detailsv'),
    re_path(r'^details/(?P<id>[0-9]+)/update/$',
            views.updateview, name='updatev'),
    re_path(r'^details/(?P<id>[0-9]+)/delete/$',
            views.deleteview, name='deletev'),
    path("signup/", views.signup.as_view(), name="signin"),
    path("login/", views.login.as_view(), name='login'),
    path("logout/", views.logout.as_view(), name='logout')

]
