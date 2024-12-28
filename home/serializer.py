from home.models import *
from rest_framework.serializers import ModelSerializer


class Custometserializer(ModelSerializer):
    class Meta:
        model=Customer
        fields="__all__"

    


class Productserializer(ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
    
class ContactMechserializer(ModelSerializer):
    class Meta:
        model=ContactMech
        fields="__all__"
    

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"

class OrderHeaderSerializer(ModelSerializer):
    
    class Meta:
        model = OrderHeader
        fields = "__all__"
    
    def create(self, validated_data):
        order_date = validated_data['order_date']
        billing_contact_mech=validated_data['billing_contact_mech']
        shipping_contact_mech=validated_data['shipping_contact_mech']
        customer=validated_data['customer']
        obj=OrderHeader.objects.create(
            order_date=order_date,
            billing_contact_mech=billing_contact_mech,
            shipping_contact_mech=shipping_contact_mech,
            customer=customer
        )    

        return obj

class toOrderHeaderSerializer(ModelSerializer):
    
    class Meta:
        model = OrderHeader
        fields = "__all__"


        
        