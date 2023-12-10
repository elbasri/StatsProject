# stats_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('result/<int:result_id>/', result_view, name='result_view'),
    path('', home, name='home'),
    path('', include(router.urls)),
    path('api/uploaded-files/', UploadedFileListCreate.as_view(), name='uploaded-files-list'),
    path('counts/', get_statistics, name='get_statistics'),
    path('api/apply-algorithm/', ApplyAlgorithm.as_view(), name='apply_algorithm'),
    path('api/results/', ResultListCreateView.as_view(), name='result-list-create'),
    path('api/results/<int:pk>/', ResultRetrieveView.as_view(), name='result-retrieve'),
]
