from rest_framework import serializers 
from bookInventorys.models import BookInventory
 
 
class BookInventorySerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BookInventory
        fields = ('id',
                  'title',
                  'author',
                  'dateCreated',
                  'published')