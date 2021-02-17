# Importing django rest framework's generics views
from rest_framework import generics
# Importing our Todo Model
from .models import Todo
# Importing our serializer
from .serializers import TodoSerializer

# Only difference (besides minor naming schemes) between django and rest is we need to add a serializers.py and we do not need a templates file.

# We'll use ListAPIView to display all todos
class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
# We'll use RetrieveAPIView to display a single instance
class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer