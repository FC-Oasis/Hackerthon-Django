from django.db import models


class Record(models.Model):
    humidity = models.IntegerField()
    temperature = models.IntegerField()
    recorded_at = models.DateTimeField(
        unique=True,
    )

    class Meta:
        ordering = ('-recorded_at',)
