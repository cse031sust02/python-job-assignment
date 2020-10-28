from django.urls import path

from . import views

app_name = 'progress_demo'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_progress/<task_id>', views.get_progress, name='task_status'),
]