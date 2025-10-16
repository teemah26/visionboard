# boards/api_views.py
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .models import Board, Item
from .serializers import UserSerializer, BoardSerializer, ItemSerializer

# User Registration
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# Boards
class BoardListCreateView(generics.ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)


# Items
class ItemListCreateView(generics.ListCreateAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(board__owner=self.request.user)

    def perform_create(self, serializer):
        board = serializer.validated_data["board"]
        if board.owner != self.request.user:
            raise PermissionError("You do not own this board.")
        serializer.save()


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Item.objects.filter(board__owner=self.request.user)
