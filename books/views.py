# from django.shortcuts import render
# #from django.views.generic import ListView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from .models import Book
# from .forms import BookForm
# # Create your views here.

# class BookListView(ListView):
#     model = Book
#     paginate_by = 10

# class BookCreateView(CreateView):
#     model = Book
#     form_class = BookForm

#     #fields = ['title', 'author', 'genre', 'published_date']
#     success_url = reverse_lazy('book_list')

# class BookUpdateView(UpdateView):
#     model = Book
#     form_class = BookForm
#     #fields = ['title', 'author', 'genre', 'published_date']
#     success_url = reverse_lazy('book_list')

# class BookDeleteView(DeleteView):
#     model = Book
#     success_url = reverse_lazy('book_list')
 

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BookUpdateAPIView(generics.RetrieveUpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)