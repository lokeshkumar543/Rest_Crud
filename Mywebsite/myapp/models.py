from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    discription=models.TextField()
    brand=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
        return self.title 