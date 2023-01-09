from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=500)
    slug = models.CharField(max_length=300)
    description = models.TextField()

    def _str_(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='groups'
    )
