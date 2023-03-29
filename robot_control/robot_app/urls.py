from django.urls import path
from . import views

# URLConf
urlpatterns = [
     path('move/', views.control_robot)
]
