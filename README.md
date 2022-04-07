<h1 align="center">Documentação 📄</h1>

<p align="center">
<p align="center">📚 Projeto simples de uma biblioteca feito utilizando o framework Django 📚.</p>

<hr>
<p align='center'>
  <img src="https://user-images.githubusercontent.com/84135240/162264506-b6a0b116-10bf-4d6d-be79-845539efb573.gif"=/>
</p>

<h2>🏁 Tópicos</h2>

<!--ts-->
   * [Tecnologias Usadas](#req) 🚀
   * [Criando o Projeto e a Aplicação](#CPA) 🔨 
   * [Configurando o Arquivo settings.py](#CAS) 👷
   * [Preparando o Banco de Dados](#BD) 🎲 
   * [Criando o Modelo](#CM) 💢 
   * [Registrando o Modelo na Administração do Django](#RMAD) 📝 
   * [Fazendo as Migrações do Banco de Dados](#FMBD) ✅ 
   * [Criando o Super Usuário para Administração do Django](#CSUAD) 🔑 
   * [Criando o Formulário do Modelo](#CFM) 📝
   * [Criando as Views](#CV) 🎯 
   * [Criando as Rotas](#CR) ↩️ 
   * [Criando o Template do Projeto](#CTP) ™️ 
<!--te-->
<hr>
<h2 id="req"> 🚀 Tecnologias Usadas</h2>
- ✅ Python <br>
- ✅ Django Framework<br>
- ✅ PostgreSQL <br>
- ✅ HTML <br>
- ✅ Bootstrap <br>
- ✅ Visual Studio Code <br>

<hr>

<h2 id="CPA">🔨 Criando o Projeto e a Aplicação</h2>

<p>📣 No terminal/cmd, navegue até o diretório do arquivo e</p>

<p>1️⃣ Digite o seguinte comando para criar o projeto:</p>

```bash
django-admin startproject projeto_biblioteca .
```

<p>2️⃣ Digite o seguinte comando para criar a aplicação:</p>

```bash
django-admin startapp app_biblioteca
```
<hr>
<h2 id="CAS">👷 Configurando o Arquivo settings.py</h2>

<p>1️⃣ Importe o módulo 'os' logo no início do arquivo <code>settings.py</code></p>

```python
import os
```

<p>2️⃣ Adicione os aplicativos do projeto na variável INSTALLED_APPS</p>

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app_biblioteca',   # Aplicativo adicionado 01
    'bootstrap4',       # Aplicativo adicionado 02
]
```

<p>3️⃣ Na variável TEMPLATES, na chave DIRS, adicione o valor 'templates' na lista.
    
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # Valor 'templates' adicionado a chave DIRS.
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
    
<p>4️⃣ Na variável LANGUAGE_CODE, modifique o valor para 'pt-br'
    
```python
LANGUAGE_CODE = 'pt-br'
```
    
 <p>5️⃣ Na variável TIME_ZONE, modifique o valor para 'America/Sao_Paulo'
    
```python
TIME_ZONE = 'America/Sao_Paulo'
```
   
<hr>

<h2 id="BD">🎲 Preparando o Banco de Dados</h2>

<p>1️⃣ No arquivo settings.py, na variável DATABASES faça as seguintes configurações:</p>

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome da database',
        'USER': 'nome do usuário',
        'PASSWORD': 'senha do usuário',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
<hr>
<h2 id="CM">💢 Criando o Modelo</h2>

<p>1️⃣ No arquivo <code>models.py</code> da aplicação, digite os seguintes códigos:</p>

```python
from django.db import models

DISPONIVEL = (
    ('Sim', 'Sim'),
    ('Não', 'Não')
)

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100) 
    editora = models.CharField(max_length=100) 
    edicao = models.CharField('Edição', max_length=100)
    ano_publicacao = models.DateField('Ano da Publicação (dd/mm/aaaa)', auto_now_add=False) 
    estoque = models.IntegerField()
    disponivel = models.CharField('Disponível', max_length=3, choices=DISPONIVEL)

    def __str__(self):
        return self.nome
```
<hr>
<h2 id="RMAD">📝 Registrando o Modelo na Administração do Django</h2>

<p>1️⃣ No arquivo <code>admin.py</code> da aplicação, digite os seguintes códigos:</p>

```python
from django.contrib import admin

from app_biblioteca.models import Livro

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'autor', 'editora', 'edicao', 'ano_publicacao', 'estoque', 'disponivel')
```
<hr>
<h2 id="FMBD">✅ Fazendo as Migrações do Banco de Dados</h2>

<p>📣 No terminal/cmd, navegue até o diretório do arquivo e</p>

<p>1️⃣ Digite o seguinte comando para criar as migrações:</p>

```bash
python manage.py makemigrations
```

<p>2️⃣ Digite o seguinte comando para fazer as migrações:</p>

```python
python manage.py migrate
```

<hr>
<h2 id="CSUAD">🔑 Criando o Super Usuário para Administração do Django</h2>

<p>📣 No terminal/cmd, navegue até o diretório do arquivo e</p>

<p>1️⃣ Digite o seguinte comando para criar o super usuário:</p>

```bash
python manage.py createsuperuser
```
<hr>
<h2 id="CFM">📝 Criando o Formulário do Modelo</h2>

<p>1️⃣ Crie um arquivo chamado <code>forms.py</code> no diretório da aplicação</p>
<p>2️⃣ Digite os seguintes códigos nesse arquivo.</p>

```python
from django import forms

from app_biblioteca.models import Livro

class LivroModelForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = '__all__'
```
<hr>
<h2 id="CV">🎯 Criando as Views</h2>

<p>1️⃣ No arquivo <code>views.py</code> da aplicação digite os seguintes códigos</p>

```python
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
```
<hr>
<h2 id="CR">↩️ Criando as Rotas</h2>

<p>1️⃣ No arquivo <code>urls.py</code> do projeto faça as seguintes configurações:</p>

```python
from django.contrib import admin
from django.urls import path, include               # Importação do módulo include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_biblioteca.urls')),       # Criação de um path.
]
```

<p>2️⃣ Crie um arquivo chamado <code>urls.py</code> na aplicação e digite os seguintes códigos:</p>

```python
from django.urls import path 
from app_biblioteca.views import IndexView, CreateLivroView, UpdateLivroView, DeleteLivroView, DetailLivroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateLivroView.as_view(), name='create_livro'),
    path('<int:pk>/update/', UpdateLivroView.as_view(), name='update_livro'),
    path('<int:pk>/delete/', DeleteLivroView.as_view(), name='delete_livro'),
    path('<int:pk>/detail/', DetailLivroView.as_view(), name='detail_livro'),
]
```
<hr>
<h2 id="CTP">™️ Criando o Template do Projeto ™️</h2>

<p>1️⃣ Crie um diretório chamado <code>templates</code> no diretório da aplicação</p>
<p>2️⃣ Crie um arquivo chamado <code>base.html</code> no diretório templates e digite os seguintes códigos</p>

```html
{% load bootstrap4 %}
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    {% bootstrap_css %}
    <title>Biblioteca</title>
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
{% bootstrap_javascript jquery='full' %}
</body>
</html>
```

<p>3️⃣ Crie um arquivo chamado <code>index.html</code> no diretório templates e digite os seguintes códigos</p>

```html
{% extends 'base.html' %}
{% block content %}
    <div class="row">
        <h1>Livros</h1>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nome</th>
                    <th>Autor</th>
                    <th>Editora</th>
                    <th>Edição</th>
                    <th>Ano da Publicação</th>
                    <th>Estoque</th>
                    <th>Disponível</th>
                    <th>Ação</th>
                </tr>
            </thead>
            <tbody>
                {% for livro in livros %}
                    <tr>
                        <td>{{ livro.id }}</td>
                        <td>{{ livro.nome }}</td>
                        <td>{{ livro.autor }}</td>
                        <td>{{ livro.editora }}</td>
                        <td>{{ livro.edicao }}</td>
                        <td>{{ livro.ano_publicacao }}</td>
                        <td>{{ livro.estoque }}</td>
                        <td>{{ livro.disponivel }}</td>
                        <td>
                            <a class="btn btn-warning" href="{% url 'detail_livro' livro.id %}" style="background-color: blue; color: white; border-color: blue;" >Detalhes</a>
                            <a class="btn btn-warning" href="{% url 'update_livro' livro.id %}">Editar</a>
                            <a class="btn btn-danger" href="{% url 'delete_livro' livro.id %}">Deletar</a>
                        </td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>

    <div class="new">
        <a class="btn btn-warning" href="{% url 'create_livro' %}" style="background-color: green; color: white; border-color: green;">Novo</a>
    </div>
{% endblock %}
```

<p>4️⃣ Crie um arquivo chamado <code>livro_form.html</code> no diretório templates e digite os seguintes códigos:</p>

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
    <h1>Livros</h1>
    <form method="POST">
        {% csrf_token %%}
        {% bootstrap_form form %}
            {% buttons %}
                <button type="submit" class="btn btn-primary">Salvar</button>
                <button type="button" class="btn btn-warning">
                    <a href="{% url 'index' %}" style="color: white;">Cancelar</a>
                </button>
            {% endbuttons %}
    </form>
{% endblock %}
```

<p>5️⃣ Crie um arquivo chamado <code>livro_del.html</code> no diretório templates e digite os seguintes códigos:</p>

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
    <form method="POST">
        {% csrf_token %}
        <p>Deseja realmente deletar o livro {{ object }} ?</p>
        {% buttons %}
            <button type="submit" class="btn btn-danger">Confirmar</button>
            <button type="button" class="btn btn-warning">
                <a href="{% url 'index' %}">Cancelar</a>
            </button>
        {% endbuttons %}
    </form>
{% endblock %}
```

<p>6️⃣ Crie um arquivo chamado <code>livro_detail.html</code> no diretório templates e digite os seguintes códigos:</p>

```html
{% extends 'base.html' %}
{% load bootstrap4 %}
{% block content %}
<div class="row">
    <h1>Livros</h1>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nome</th>
                <th>Autor</th>
                <th>Editora</th>
                <th>Edição</th>
                <th>Ano da Publicação</th>
                <th>Estoque</th>
                <th>Disponível</th>
            </tr>
        </thead>
        <tbody>
                <tr>
                    <td>{{ livro.id }}</td>
                    <td>{{ livro.nome }}</td>
                    <td>{{ livro.autor }}</td>
                    <td>{{ livro.editora }}</td>
                    <td>{{ livro.edicao }}</td>
                    <td>{{ livro.ano_publicacao }}</td>
                    <td>{{ livro.estoque }}</td>
                    <td>{{ livro.disponivel }}</td>
        </tbody>
    </table>
</div>

<div class="new">
    <a class="btn btn-warning" href="{% url 'index' %}" style="background-color: green; color: white; border-color: green;">Voltar</a>
</div>
{% endblock %}
```
