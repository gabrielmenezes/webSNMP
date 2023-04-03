from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:device_id>/", views.selectOid, name="selectOid"),
    path("<int:device_id>/<int:oid_id>/", views.viewGraph, name="viewGraph")
]
