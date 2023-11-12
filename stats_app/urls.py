# stats_app/urls.py
from django.urls import path
from .views import upload_file, result_view, home

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('result/<int:result_id>/', result_view, name='result_view'),
    path('', home, name='home'),
]
