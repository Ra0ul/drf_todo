from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from todo.models import Todo
from todo.serializers import TodoSerializer


class TodoDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
        # return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
