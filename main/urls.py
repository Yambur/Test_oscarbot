"""from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
#router.register(r'main', views.TaskListView)
#router.register(r'main', views.TaskDetailView)

router.register(r'tasks', views.TaskListView, basename='tasks')
router.register(r'tasks/<int:pk>', views.TaskDetailView, basename='task')
router.register(r'shared/<int:pk>', views.SharedTaskView, basename='shared_task')

urlpatterns = [
    path('', include(router.urls)),
    path('main/task', views.TaskDetailView, basename='task'),
    path('main/shared_task', views.SharedTaskView, basename='shared_task'),
]
"""
from django.urls import path, include
from rest_framework import routers

from main import views
from main.apps import MainConfig

app_name = MainConfig.name

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='tasks')
router.register(r'tags', views.TagViewSet, basename='tags')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<uuid:uuid>/', views.SharedTaskDetail.as_view()),
    path('tasks/search/', views.TaskSearch.as_view()),
]
