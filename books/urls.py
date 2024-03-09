 
from django.urls import path
from .views import BookListAPIView, BookCreateAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
#     path('<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
#     path('<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book_delete'),
]
