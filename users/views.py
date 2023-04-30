from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


from users.serializers import CustomTokenObtainPairSerializer, UserSerializer


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True) - 아래를 요렇게 한줄로도 가능!
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({"message": "로그인확인!"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "프로필 수정 완료!"}, status=status.HTTP_201_CREATED)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "탈퇴 완료!"}, status=status.HTTP_201_CREATED)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
