from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
            
        }

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        author = cleaned_data.get('author')
        
        if not title:
            self.add_error('title', 'Title is required.')

        if not author:
            self.add_error('author', 'Author is required.')
