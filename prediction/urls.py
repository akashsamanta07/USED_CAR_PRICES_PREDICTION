from django.urls import path
from prediction import views

urlpatterns = [
    path("", views.homepage,name='index'),
    path("pred/",views.pred,name='pred'),
]