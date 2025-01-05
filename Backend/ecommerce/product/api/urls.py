from django.urls import path,include
from ..api.category_view import CategoryAPIView, CategoryDetailAPIView
from product.api.views import Productlist, ProductEdit 
from product.api.views import Commentlist, CommentEdit
from product.api.views import Reviewlist, ReviewEdit

urlpatterns = [
    path("category/", CategoryAPIView.as_view(), name="category-list"),
    path("category/<int:pk>", CategoryDetailAPIView.as_view(), name="category-detail"),

    path('productlist/', Productlist.as_view(), name="productlist"),
    path('productedit/<int:pk>/',ProductEdit.as_view(), name="productedit"),
    path('commentlist/', Commentlist.as_view(), name="commentlist"),
    path('commentedit/<int:pk>/', CommentEdit.as_view(), name="commentedit"),
    path('reviewlist/', Reviewlist.as_view(), name="reviewlist"),
    path('reviewedit/<int:pk>/', ReviewEdit.as_view(), name="reviewedit"),

]
