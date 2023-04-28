from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


from users.serializers import CustomTokenObtainPairSerializer, UserSerializer


class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(data=request.data)
        return Response({"message": "로그인 상태입니다"}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True) - 아래를 요렇게 한줄로도 가능!
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
