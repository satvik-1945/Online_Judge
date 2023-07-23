from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage,name= 'home'),
    path('problem/<int:problem_id>', views.problem_description,name= 'problem_description'),   
    path('problem/<int:problem_id>/verdict', views.submit_code,name="verdict"),
]