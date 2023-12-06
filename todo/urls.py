
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name="home"),
    path('remove/<int:id>/', views.remove, name='remove'),
    path('complete/<int:id>/', views.complete, name='complete')

]
