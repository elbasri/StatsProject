# stats_app/urls.py
from django.urls import path, include
from .views import upload_file, result_view, home
from rest_framework.routers import DefaultRouter
from .views import StatsprjlViewSet

router = DefaultRouter()
router.register(r'Statsprj', StatsprjlViewSet)

urlpatterns = [
    path('upload/', upload_file, name='upload'),
    path('result/<int:result_id>/', result_view, name='result_view'),
    path('', home, name='home'),
    path('', include(router.urls)),
]
