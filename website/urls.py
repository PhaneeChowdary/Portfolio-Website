from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('project_diabetes', views.project_diabetes, name="project_diabetes"),
    path('project_iris', views.project_iris, name="project_iris"),
    path('project_heart', views.project_heart, name="project_heart"),
    path('project_titanic', views.project_titanic, name="project_titanic"),
    path('titanic_submit', views.titanic_submit, name="titanic_submit"),
    path('diabetes_submit', views.diabetes_submit, name="diabetes_submit"),
    path('iris_submit', views.iris_submit, name="iris_submit"),
    path('heart_submit', views.heart_submit, name='heart_submit'),
]
