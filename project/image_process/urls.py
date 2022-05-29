from argparse import Namespace
from django.urls import path
from image_process import views

app_name = 'image_process'

urlpatterns = [
    path('index', views.index,name = 'index'),
    path("expression", views.expression, name="expression"),
    path("dummy", views.dummy, name="dummy"),
    path('get-emotion',views.get_emotion_from_cam,name="get-emotion"),
]
