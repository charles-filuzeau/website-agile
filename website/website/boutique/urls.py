from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('trainings', views.trainings, name='trainings'),
        # ex: /polls/5/
    path('course/<str:name>/', views.course, name='course'),
]
