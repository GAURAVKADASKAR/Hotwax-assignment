"""
URL configuration for hotwax project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import EnterTheCustomer,GetOrderByColor,updatetoadd,EnterTheProduct, EnterContactMech, CreateOrderView,orderdetails, UpdateOrderItem

urlpatterns = [
    path('customers/', EnterTheCustomer.as_view()),
    path('products/', EnterTheProduct.as_view()),
    path('contactmech/', EnterContactMech.as_view()),
    path('orders/', CreateOrderView.as_view()),
    path('orders/<int:id>/', orderdetails.as_view()),
    path('orders/<int:order_id>/items/<int:order_item_seq_id>/', UpdateOrderItem.as_view()),
    path('orders/<int:order_id>/items/',updatetoadd.as_view()),
    path('GetOrderByColor/',GetOrderByColor.as_view())

]



