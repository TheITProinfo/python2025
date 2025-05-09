# this is the views.py file for the order app.
from django.http import HttpResponse
from django.shortcuts import redirect, render
## import database models Order
from .models import Order
from .form import OrderForm

# Create your views here.
def order_list(request):
    # return HttpResponse("This is the order view")
    
    # Fetch all orders from the database, sorted by creation date (newest first)
    orders = Order.objects.all().order_by('-created_at')
    
    return render(request, 'order/order_list.html', {'orders': orders})
def create_order(request):
    # order=Order.objects.create(customer_name='John Doe', total_amount=1245.00)
    # order.save()
    # return HttpResponse("This is the create order view, successfully")
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')  # Make sure this name exists in your urls
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html', {'form': form})
def update_order(request, order_id):
    order = Order.objects.get(id=1)
    order.total_amount = 5000.00
    order.save()
    return HttpResponse("This is the update order view for order id: " + str(order_id))
def delete_order(request, order_id):
    return HttpResponse("This is the delete order view for order id: " + str(order_id))
