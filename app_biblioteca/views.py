from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from app_biblioteca.models import Livro
from app_biblioteca.forms import LivroModelForm

class IndexView(ListView):
    models = Livro
    template_name = 'index.html'
    queryset = Livro.objects.all()
    context_object_name = 'livros'

class CreateLivroView(CreateView):
    models = Livro
    template_name = 'livro_form.html'
    queryset = Livro.objects.all()
    fields = ['nome', 'autor', 'editora', 'edicao', 'ano_publicacao', 'estoque', 'disponivel']
    success_url = reverse_lazy('index')

class UpdateLivroView(UpdateView):
    models = Livro
    template_name = 'livro_form.html'
    queryset = Livro.objects.all()
    fields = ['nome', 'autor', 'editora', 'edicao', 'ano_publicacao', 'estoque', 'disponivel']
    success_url = reverse_lazy('index')

class DeleteLivroView(DeleteView):
    models = Livro
    template_name = 'livro_del.html'
    queryset = Livro.objects.all()
    success_url = reverse_lazy('index')
    
    class DetailLivroView(DetailView):
    template_name = 'livro_detail.html'
    queryset = Livro.objects.all()
