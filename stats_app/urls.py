# stats_app/urls.py
from django.urls import path, include
from .views import upload_file, result_view, home
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('result/<int:result_id>/', result_view, name='result_view'),
    path('', home, name='home'),
    path('', include(router.urls)),
    path('api/uploaded-files/', UploadedFileListCreate.as_view(), name='uploaded-files-list'),
    path('api/results/', ResultListCreate.as_view(), name='results-list'),
    path('counts/', get_statistics, name='get_statistics'),
]
