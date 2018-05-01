from django.db import models
from django.urls import reverse

class Garage(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    
    def __str__(self):
        return "{} {}".format(self.name, self.capacity)

class Car(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    garage = models.ForeignKey(
        Garage, 
        on_delete=models.CASCADE, 
        related_name='cars',
        related_query_name='car'
    )
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myapp:car_details', args=[str(self.pk)])
