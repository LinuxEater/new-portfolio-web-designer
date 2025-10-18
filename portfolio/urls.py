from django.urls import path
from .views import home, budget, projects, submit_budget_form, budget_success

urlpatterns = [
    path('', home, name='home'),
    path('budget/', budget, name='budget'),
    path('projects/', projects, name='projects'),
    path('submit_budget_form/', submit_budget_form, name='submit_budget_form'),
    path('budget_success/', budget_success, name='budget_success'),
]
