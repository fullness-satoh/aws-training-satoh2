from django.urls import path
from .views import ReviewTopView
from .views import ProductListView
from .views import ReviewListView
from .views import ProductDetailView
from .views import ReviewDetailView
from .views import CreateReviewView
from .views import UpdateReviewView
from .views import DeleteReviewView

app_name = 'review'

urlpatterns = [
    path('review-top', ReviewTopView.as_view(), name='review-top'),
    path('product-list', ProductListView.as_view(), name='product-list'),
    path('review-list', ReviewListView.as_view(), name='review-list'),
    path('product-detail/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('review-detail/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('create-review', CreateReviewView.as_view(), name='create-review'),
    path('update-review/<int:pk>/', UpdateReviewView.as_view(), name='update-review'),
    path('delete-review/<int:pk>/', DeleteReviewView.as_view(), name='delete-review'),
]
