from django.contrib import admin

from app_biblioteca.models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'editora', 'edicao', 'ano_publicacao', 'estoque', 'disponivel')