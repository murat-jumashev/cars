from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    