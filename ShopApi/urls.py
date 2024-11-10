from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # categories
    path('api/v1/categories/', views.categories_view),
    path('api/v1/categories/<int:id>/', views.category_detail_view),

    # products
    path('api/v1/products/', views.products_view),
    path('api/v1/products/<int:id>/', views.product_detail_view),

    # reviews
    path('api/v1/reviews/', views.reviews_view),
    path('api/v1/reviews/<int:id>/', views.review_detail_view),
]
