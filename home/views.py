from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.serializer import *
import json
from .models import OrderHeader, OrderItem


class EnterTheCustomer(APIView):
    def post(self, request):
        serializer = Custometserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EnterTheProduct(APIView):
    def post(self, request):
        serializer = Productserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "success"}, status=status.HTTP_200_OK)
        return Response({"message": "failed", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class EnterContactMech(APIView):
    def post(self, request):
        serializer = ContactMechserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateOrderView(APIView):
     def post(self, request):
        serializer = OrderHeaderSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save()
         
            for item_data in request.data['order_items']:
                OrderItem.objects.create(
                    order=order,  
                    quantity=item_data['quantity'],
                    product= Product.objects.get(product_id=item_data['product']),
                    status=item_data['status']
                )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class orderdetails(APIView):
    def get(self, request, id):
        try:
            obj = OrderHeader.objects.get(order_id=id)
            serializer = OrderItemSerializer(obj.orderitem_set.all(), many=True)
            return Response({'status': status.HTTP_200_OK, 'data': serializer.data})
        except OrderHeader.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            obj = OrderHeader.objects.get(order_id=id)
            obj1 = OrderItem.objects.filter(order=obj)
            obj1.delete()
            obj.delete()
            return Response({'status': status.HTTP_204_NO_CONTENT})
        except OrderHeader.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,id):
        obj=OrderHeader.objects.get(order_id=id)
        serializer=OrderHeaderSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': status.HTTP_204_NO_CONTENT})
        else:
             return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)


class UpdateOrderItem(APIView):
    def put(self, request, order_id, order_item_seq_id):
        obj1=OrderItem.objects.get(order_item_seq_id=order_item_seq_id,order_id=order_id)
        obj2=OrderItemSerializer(obj1,data=request.data,partial=True)
        if obj2.is_valid():
            obj2.save()
            return Response({'status':obj2.data})


    def delete(self, request, order_id, order_item_seq_id):
        try:
            order_item = OrderItem.objects.get(order_item_seq_id=order_item_seq_id, order__order_id=order_id)
            order_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except OrderItem.DoesNotExist:
            return Response({'message': 'OrderItem not found'}, status=status.HTTP_404_NOT_FOUND)
    
class updatetoadd(APIView):
    def get(self,request,order_id):
        obj=OrderItem.objects.filter(order_id=order_id).first()
        obj1=OrderItemSerializer(obj)
        new_data=obj1.data
      
        return Response({'data':obj1.data})
    

class GetOrderByColor(APIView):
    def post(self,request):
        color=request.data['color']
        obj=OrderItem.objects.filter(product__color=color)
        serializer=OrderItemSerializer(obj,many=True)
        if obj:
            return Response({'status':status.HTTP_200_OK,'data':serializer.data})
    

