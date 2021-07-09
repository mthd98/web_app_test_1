from typing_extensions import runtime
from django.db import models
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    location = models.CharField(max_length=300)
    image=models.ImageField(upload_to='images',null=True)
    


    def get_abs_url(self):
        return reverse('product-detail-page',kwargs={'id':self.id})

    