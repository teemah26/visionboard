"""""
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Board,Item
from .forms import ItemForm
from .serializers import BoardSerializer, ItemSerializer
from rest_framework import viewsets, permissions

@login_required
def dashboard(request):
    boards = Board.objects.prefetch_related("items").all()
    return render(request, "boards/dashboard.html", {"boards": boards})

def board_detail(request, board_id):
    board = get_object_or_404(Board, id=board_id, user=request.user)
    items = board.item_set.all()
    return render(request, "boards/board_detail.html", {"board": board, "items": items})
def add_board(request):
    if request.method == "POST":
        title = request.POST.get("title")
        if title:
            Board.objects.create(user=request.user, title=title)
            return redirect("dashboard")  # after creating, go back to dashboard
    return render(request, "boards/add_board.html")

def add_item(request, board_id):
    board = get_object_or_404(Board, id=board_id)
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.board = board
            item.save()
            return redirect("dashboard")
    else:
        form = ItemForm()
    return render(request, "boards/add_item.html", {"form": form, "board": board})

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]"""""

# boards/views.py
from rest_framework import viewsets
from .models import Board, Item
from .serializers import BoardSerializer, ItemSerializer

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
