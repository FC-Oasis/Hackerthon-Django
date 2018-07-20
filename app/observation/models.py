from django.db import models


class Record(models.Model):
    humidity = models.IntegerField()
    temperature = models.IntegerField()
    recorded_at = models.DateTimeField(
        unique=True,
    )

    class Meta:
        ordering = ('-recorded_at',)

    def __str__(self):
        return f'Record : humidity {self.humidity}, temperature {self.temperature}, recorded_at {self.recorded_at}'
