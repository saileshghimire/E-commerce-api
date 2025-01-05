from django.contrib import admin
from product.models import Product, Comment,Category, SubCategory,Order,OrderItem,CartItem,Cart,Review
# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Comment)
