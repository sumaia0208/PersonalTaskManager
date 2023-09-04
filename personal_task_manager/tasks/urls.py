from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name="task_home"),
    path("create/", views.create_task, name="create-task"),
    path("detail/<pk>/", views.task_detail, name="detail-task"),
    path("update/<pk>/", views.update_task, name="update-task"),
    path("delete/<pk>/", views.delete_task, name="delete-task"),
]
