from django.test import TestCase

# Create your tests here.


# class OrderListSerializer(ModelSerializer):

#     profile_name = SerializerMethodField()
#     item_title = SerializerMethodField()
#     item_price = SerializerMethodField()

#     def get_profile_name(self, profile):
#         return profile.user.username
    
#     def get_item_title(self, item):
#         return item.title
    
#     def get_item_price(self, item):
#         return item.price

#     class Meta:
#         model = Order
#         fields = ('id', 'profile_name', 'item_title', 'item_price')

# class CategorySerializer(ModelSerializer):

#     items = serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True,
#         view_name='mobile-detail'
#     )

#     class Meta:
#         model = Category
#         fields = ('name', 'url', 'items')
#         read_only_fields = fields