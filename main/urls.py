from django.urls import path
from main.apps import MainConfig
from main import views


app_name = MainConfig.name

urlpatterns = [
    path('', views.main, name='main_page'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.ProjectTagListView.as_view(), name='projects')
]
