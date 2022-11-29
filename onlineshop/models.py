from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.
class Product(models.Model):
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    def __str__(self):
        return self.title
class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img = models.ImageField(default='no_image.jpg', upload_to='product_image')
    availability = models.BooleanField()
    
    def _str_(self):
        return self.name