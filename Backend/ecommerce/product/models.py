from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
# from Backend.ecommerce.ecommerce import settings


# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE,related_name="category")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField()
    # Stock Keeping Unit
    sku = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='products_images/', blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_discounted_price(self):
        if self.discount_price:
            return self.discount_price
        return self.price
    
    def is_in_stock(self):
        return self.stock_quantity > 0
    

class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    review_product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="review_product")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviewer_user')
    created_at = models.DateTimeField(auto_now_add=True)
    updateda_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review for {self.review_product.name} by {self.user.email}"


class Comment(models.Model):
    comment = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_comment")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="commenter_user")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_comment.name
    

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order_user")
    creted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.email}"
    
    def get_total_price(self):
        total_price = 0
        for item in self.cart_items.all():
            total_price = sum(item.product.get_discounted_price() * item.quantity)
            return total_price
        
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name="cart_items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creted_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    shipping_address = models.TextField()
    status = models.CharField(max_length=50, choices=[('pending','Pending'),('shipped','Shipped'),('delivered','Delivered')])


    def __str__(self):
        return f"Order {self.id} by {self.user.email}"

    def update_total_price(self):
        total = sum(item.product.get_discounted_price() * item.quantity for item in self.order_items.all())
        self.total_price = total
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
    def save(self):
        self.price_at_purchase =self.product.get_discounted_price()
        # self.save()
        super().save()
    