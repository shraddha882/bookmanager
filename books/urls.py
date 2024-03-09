# from django.urls import path
# #from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView
# from .views import BookListAPIView, BookDetailAPIView

# urlpatterns = [
#     #path('', BookListView.as_view(), name='book_list'),
#     #path('create/', BookCreateView.as_view(), name='book_create'),
#     #path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
#     #path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
#      
# ]
from django.urls import path
from .views import BookListAPIView, BookCreateAPIView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('create/', BookCreateAPIView.as_view(), name='book_create'),
#     path('<int:pk>/update/', BookUpdateAPIView.as_view(), name='book_update'),
#     path('<int:pk>/delete/', BookDeleteAPIView.as_view(), name='book_delete'),
]
