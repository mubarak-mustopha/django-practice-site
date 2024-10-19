from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=128)
    image_url = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
