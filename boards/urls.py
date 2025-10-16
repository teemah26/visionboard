

""""from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('board/<int:pk>/', views.board_detail, name='board_detail'),
    path('board/add/', views.add_board, name='add_board'),
    path('board/<int:board_id>/add_item/', views.add_item, name='add_item'),
]"""

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import BoardViewSet, ItemViewSet



router = DefaultRouter()
router.register(r'boards', BoardViewSet, basename='board')
router.register(r'items', ItemViewSet, basename='item')

urlpatterns = router.urls
