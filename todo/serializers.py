from rest_framework import serializers
from todo.models import Todo


class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "is_complete")


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Todo
        fields = ("pk", "title", "is_complete", "created_at",
                  "updated_at", "completion_at", "user")
