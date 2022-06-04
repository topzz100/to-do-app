from django.urls import path
from . import views

urlpatterns = [
  path('', views.taskList, name='tasks')
]


# urlpatterns = [
#     path('', views.index, name='index'),
# ]