from django.conf.urls import url
from . import views

urlpatterns = [

    # displays users trips and other's trips
    url(r'^$', views.travels, name='travels'),

    # page with add trip form on it
    url(r'^add$', views.add, name='add'),
    url(r'^join$', views.join, name='join'),

    # route to handle form data from add page
    url(r'^process$', views.process, name='process'),
]