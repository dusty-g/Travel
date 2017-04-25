from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<destinationID>\d+)', views.destination),
]