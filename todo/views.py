from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response


class TodoDetailView(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
        # return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
