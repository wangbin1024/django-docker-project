from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

app_name = 'app'

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('create-task/', TaskCreate.as_view(), name="create"),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name="update"),
    path('delete-task/<int:pk>/', TaskDelete.as_view(), name="delete"),
]   