from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("matriz/<int:pk>", views.detail, name = "detail"),
]
