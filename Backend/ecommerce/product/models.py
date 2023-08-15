from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    comment = models.TextField()
    product_comment = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comment")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_comment.name
    
