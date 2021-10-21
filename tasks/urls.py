from django.urls import path
from django.urls.conf import include

from .views import add_task, index

app_name = "tasks"

urlpatterns = [
  path('', index, name="index"),
  path('add_task', add_task, name="add_task")
]