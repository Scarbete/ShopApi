from rest_framework.serializers import ModelSerializer
from product.models import Category, Product, Review


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price category'.split()


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text'.split()
