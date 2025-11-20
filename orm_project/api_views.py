from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Author, Category
from .serializers import AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    
    # Кастомное действие для API
    @action(detail=True, methods=['get'])
    def get_authors(self, request, pk=None):
        print('authors GET')
        authors = Author.objects.all()
        
        return Response({'data': authors})
    
    # список 
    def get_queryset(self):
        print('authors GET!!!')
        queryset = Author.objects.all()
        # published_only = self.request.query_params.get('published', None)
        # if published_only:
        #     queryset = queryset.filter(is_published=True)
        return queryset