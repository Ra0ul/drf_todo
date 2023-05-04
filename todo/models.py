from datetime import timezone
from django.db import models
from users.models import User


class Todo(models.Model):
    user = models.ForeignKey(User, verbose_name="작성자",
                             on_delete=models.CASCADE)
    title = models.CharField("할일 제목", max_length=50)
    is_complete = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성 시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정 시간", auto_now=True)
    completion_at = models.DateTimeField("완료 시간", null=True, blank=True)

    def complete(self):
        self.is_complete = True
        self.completion_at = timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)
