from django.urls import path,include
from student import views
urlpatterns = [
    # path('index',views.index),
    path('index/',views.index,name="index"),
]