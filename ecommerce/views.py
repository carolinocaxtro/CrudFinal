from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Produto

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produto_list.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Produto.objects.filter(nome__icontains=query)
        return Produto.objects.all()

class ProdutoCreateView(UserPassesTestMixin, CreateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = '/ecommerce/'
    
    def test_func(self):
        return self.request.user.is_superuser

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

class ProdutoUpdateView(UserPassesTestMixin, UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('produto_list')

    def test_func(self):
        return self.request.user.is_superuser

class ProdutoDeleteView(UserPassesTestMixin, DeleteView):
    model = Produto
    template_name = 'produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')

    def test_func(self):
        return self.request.user.is_superuser









    
