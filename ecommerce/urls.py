from django.urls import path
from .views import (
    ProdutoListView,
    ProdutoCreateView,
    ProdutoDetailView,
    ProdutoUpdateView,
    ProdutoDeleteView,
)

urlpatterns = [
    path('', ProdutoListView.as_view(), name='produto_list'),
    path('criar_produto/', ProdutoCreateView.as_view(), name='produto_create'),
    path('detalhe_produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('editar_produto/<int:pk>/', ProdutoUpdateView.as_view(), name='produto_update'),
    path('deletar_produto/<int:pk>/', ProdutoDeleteView.as_view(), name='produto_delete'),
]


