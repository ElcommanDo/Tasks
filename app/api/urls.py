from django.urls import path, include
from .views import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
