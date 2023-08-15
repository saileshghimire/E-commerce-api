from django.urls import path,include
from product.api.views import Productlist, ProductEdit


urlpatterns = [
    path('productlist/', Productlist.as_view(), name="productlist"),
    path('productedit/<int:pk>/',ProductEdit.as_view(), name="productedit"),

]
