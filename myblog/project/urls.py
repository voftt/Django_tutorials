from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('', views.project_index, name='index'),
    path('detail/<int:id>', views.project_detail, name='detail'),
]
