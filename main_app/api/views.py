from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from .serializer import ToDoSerializer
from ..models import ToDoModel, ImageTodo


class ListCreateToDoAPI(APIView):
    permission_classes = [IsAuthenticated,]
    queryset = ToDoModel.objects.all()
    
    def get(request):
        return Response()
    