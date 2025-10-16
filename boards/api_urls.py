from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import api_views

urlpatterns = [
    # Auth
    path("register/", api_views.RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Boards
    path("boards/", api_views.BoardListCreateView.as_view(), name="board_list"),
    path("boards/<int:pk>/", api_views.BoardDetailView.as_view(), name="board_detail"),

    # Items
    path("items/", api_views.ItemListCreateView.as_view(), name="item_list"),
    path("items/<int:pk>/", api_views.ItemDetailView.as_view(), name="item_detail"),
]
