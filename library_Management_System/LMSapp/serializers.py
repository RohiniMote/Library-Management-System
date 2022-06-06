from .models import Book
from rest_framework import serializers

# Create your ModelSerializer here
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"