from django.urls import path 
from app_biblioteca.views import IndexView, CreateLivroView, UpdateLivroView, DeleteLivroView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateLivroView.as_view(), name='create_livro'),
    path('<int:pk>/update/', UpdateLivroView.as_view(), name='update_livro'),
    path('<int:pk>/delete/', DeleteLivroView.as_view(), name='delete_livro'),
]