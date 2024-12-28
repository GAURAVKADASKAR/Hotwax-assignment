from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

   
class ContactMech(models.Model):
    contact_mech_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)

    


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    color = models.CharField(max_length=30, null=True, blank=True)
    size = models.CharField(max_length=10, null=True, blank=True)




class OrderHeader(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_contact_mech = models.ForeignKey(ContactMech, related_name='shipping_orders', on_delete=models.CASCADE)
    billing_contact_mech = models.ForeignKey(ContactMech, related_name='billing_orders', on_delete=models.CASCADE)


class OrderItem(models.Model):
    order_item_seq_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(OrderHeader, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)

    
