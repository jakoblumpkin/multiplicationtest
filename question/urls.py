from django.urls import path
from . import views


urlpatterns = [
    path('firstQ/', views.firstQ),
    path('', views.home),
    path('secondQ/', views.secondQ),
    path('thirdQ/', views.thirdQ),
    path('fourthQ/', views.fourthQ),
    path('gradeFourth/', views.gradeFourth),
    path('finalgrade/', views.finalGrade),
]
