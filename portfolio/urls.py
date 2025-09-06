from django.urls import path
from .views import home, budget, projects

urlpatterns = [
    path('', home, name='home'),
    path('budget/', budget, name='budget'),
    path('projects/', projects, name='projects'),
]





