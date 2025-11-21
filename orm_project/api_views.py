from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
   
    # список 
    def get_queryset(self):
        alive_only = self.request.query_params.get('alive', None)
        if alive_only:
            print('authors GET alive only')
            queryset = Author.objects.filter(alive = True) # .values('id', 'name')
            for a in queryset:
                for b in a.myBooks():
                    print(b)
        else:
            print('authors GET all')
            queryset = Author.objects.all()
            for a in queryset:
                for b in a.myBooks():
                    print(b)
        return queryset
    
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    # список 
    def get_queryset(self):
        print('books GET all')
        queryset = Book.objects.all()
        for b in queryset:
            print(b)

        return queryset