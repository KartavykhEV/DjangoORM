from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Author
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
        
        alive_only = self.request.query_params.get('alive', None)
        if alive_only:
            print('authors GET alive only')
            queryset = Author.objects.filter(alive = True)
        else:
            print('authors GET all')
            queryset = Author.objects.filter()

        return queryset