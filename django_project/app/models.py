from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

class Task(BaseModel):
    # User：ユーザーモデルを外部キーとして持つ　on_delete=models.CASCADE：ユーザーが削除されたらタスクも削除　null=True：nullを許可　blank=True：空白を許可
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = now()
        self.save()

    class Meta:
        db_table = "task"
        indexes = [
            models.Index(fields=["title"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        completed = "completed" if self.completed else "not completed"
        return self.title + " (" + completed + ")"