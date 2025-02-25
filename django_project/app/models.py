from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Member(BaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = "member"
        verbose_name = "Member"
        indexes = [
            models.Index(fields=["name"]),
        ]
        ordering = ["-created_at"]
