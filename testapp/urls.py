from django.urls import path
from testapp.views import salary_view

urlpatterns = [
    path('',salary_view, name = 'salary_view'),
]