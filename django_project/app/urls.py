from django.urls import path
from . import views
from .views import (
    TaskList,
    TaskDetail,
    TaskCreate,
    TaskUpdate,
    TaskDelete,
    TaskListLoginView,
    TaskListLogoutView,
    UserRegisterView,
    TaskListSearch,
)

app_name = "app"

urlpatterns = [
    path("login", TaskListLoginView.as_view(), name="login"),
    path("list", TaskList.as_view(), name="task_list"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    path("create-task/", TaskCreate.as_view(), name="create"),
    path("update-task/<int:pk>/", TaskUpdate.as_view(), name="update"),
    path("delete-task/<int:pk>/", TaskDelete.as_view(), name="delete"),
    path("logout", TaskListLogoutView.as_view(), name="logout"),
    path("register", UserRegisterView.as_view(), name="register"),
    path("list/", TaskListSearch.as_view(), name="search"),
]
