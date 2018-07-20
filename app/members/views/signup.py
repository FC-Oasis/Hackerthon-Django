from django.conf import settings
from django.db import models


class Comment(models.Model):
    parent_comment = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comments',
    )
    _author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    _content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment (author: {self.author.username})'

    @property
    def author(self):
        if self.is_deleted:
            return None
        return self._author

    @property
    def content(self):
        if self.is_deleted:
            return '삭제된 댓글입니다'
        return self._content

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
