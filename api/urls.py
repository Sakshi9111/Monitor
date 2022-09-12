from django.urls import path
from . import views

urlpatterns = [
    path('',views.getData),
    path('add/',views.addItem),
    path('time/',views.current_datetime),
    path('home/',views.monitor)

]
