from django.urls import path,include
from ..api.category_view import CategoryAPIView, CategoryDetailAPIView
from .product_view import ProductListView, ProductDetailView
from product.api.views import Commentlist, CommentEdit
from .review_view import ReviewListAPIView, ReviewDetailAPIView
from .cartitem_view import CartItemListAPIView, CartItemDetailAPIView

urlpatterns = [
    path("category/", CategoryAPIView.as_view(), name="category-list"),
    path("category/<int:id>", CategoryDetailAPIView.as_view(), name="category-detail"),
    path('', ProductListView.as_view(), name="productlist"),
    path('<int:id>/',ProductDetailView.as_view(), name="productedit"),

    path('comment/', Commentlist.as_view(), name="commentlist"),
    path('comment/<int:id>/', CommentEdit.as_view(), name="commentedit"),

    path('review/', ReviewListAPIView.as_view(), name="reviewlist"),
    path('review/<int:id>/', ReviewDetailAPIView.as_view(), name="reviewedit"),

    path('cartitem/', CartItemListAPIView.as_view(), name="cartitem-list"),
    path('cartitem/<int:id>/', CartItemDetailAPIView.as_view(), name="cartitem-detail"),
]
