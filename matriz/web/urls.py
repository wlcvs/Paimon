from django.urls import path

from . import views

urlpatterns = [
    path("", views.MatrizListView.as_view(), name = "matriz-list"),
    path("matriz/create", views.MatrizCreateView.as_view(), name = "matriz-create"),
    path("matriz/create/<int:pk>", views.MatrizCreateView.as_view(), name = "matriz-create"),
]
