from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('assessment',views.assessment, name='assessment'),
    path('trainings', views.trainings, name='trainings'),
    path('course/<str:name>/', views.course, name='course'),
    path('calendar',views.calendar, name='calendar'),
    path('consulting',views.consulting, name='consulting'),
]
