import sys
from django.contrib import messages
from django.shortcuts import render, redirect
#from nur_admin.models import User, Nursery
from django.utils.datetime_safe import date
from nur_admin.models import customer, Nursery
from .models import CartItem, BillingAddress, Order

def home(request):
    return render(request, 'home.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        contact = request.POST['contact']
        password = request.POST['password']
        confirm_password = request.POST['c_password']
        email = request.POST['email']

        if password == confirm_password:
            if customer.objects.filter(email=email).exists():
                messages.error(request, 'Email Already Taken')
                return redirect('/register/')
            else:
                user = customer.objects.create( password=password, email=email, contact=contact,
                                           firstname=first_name,lastname=last_name, c_password=confirm_password )
                user.save()
                print('user created')
                return redirect('/client/home/')

        else:
            messages.info(request, 'password not matching..')
            return redirect('/register/')


    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')

        val = customer.objects.filter(email=e, password=p).count()

        if val == 1:
            data = customer.objects.filter(email=e, password=p)
            for items in data:
                request.session['email'] = items.email
                request.session['id'] = items.id
                return redirect('/client/home/')

        else:
            messages.error(request, 'Invalid username and password')
        return render(request, 'login.html')
    else:

        return render(request, 'login.html')


def logout(request):
    del request.session['id']
    return redirect('/client/login/')


def shop(request):
    a = Nursery.objects.all()
    return render(request,"shop.html",{'a':a})

def shop_details(request, id):
    pro = Nursery.objects.get(id=id)
    return render(request, 'shop_details.html', {'pro':pro})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def add_to_cart(request):
    if request.method == "POST":
        u = request.session['id']
        o = request.POST['ordered']
        p = request.POST['product_id']
        print('----',p)
        q = request.POST['quantity']

        c = CartItem(user_id_id=u, ordered=o, product_id_id=p,quantity=q)
        print(c)
        c.save()
        return redirect('/client/shop/')

    else:
        pass
    return render(request, 'cart.html')


def cart(request):
    b = CartItem.objects.all()
    a = request.session['id']
    c = CartItem.objects.filter(user_id=a)
    sum = 0

    for val in c:
        sum += val.quantity * val.product_id.price
        print("___", sum)
    return render(request,"cart.html",{'c':c, 'sum':sum})


def cart_del(request, id=0):
    c = CartItem.objects.get(id=id)
    c.delete()
    return redirect('/client/cart/')

def checkout(request):
    e = request.session['id']
    c = CartItem.objects.filter(user_id=e)
    b = CartItem.objects.all()
    sum = 0

    for val in c:
        sum += val.quantity * val.product_id.price
        print("___", sum)

    if request.method == 'POST':
        try:
            u = request.session['id']
            s = request.POST['Street_Address']
            a = request.POST['Apartment_Address']
            c = request.POST['Countries']
            z = request.POST['Zip']
            city = request.POST['city']
            p = request.POST['phone']
            mail = request.POST['E_mail']

            bill = BillingAddress(user_id_id=u, Street_Address=s, Apartment_Address=a, Countries=c, Zip=z, city=city,
                                 E_mail=mail, phone=p)
            bill.save()
            print("__", bill)
            return redirect('/client/order_summary/')
        except:
            print("___", sys.exc_info())

    return render(request, 'checkout.html', {'c':c, 'sum':sum, 'b':b})


def order_summary(request):
    us = request.session['id']
    bil = BillingAddress.objects.filter(user_id=us)
    cart = CartItem.objects.filter(user_id=us)
    amount = 0.0
    total_amount = 0.0
    shipping_amount = 0.0
    cart_item = [p for p in CartItem.objects.filter(user_id=us)]
    if cart_item:
        for p in cart_item:
            temp_amount = (p.quantity * p.product_id.price)
            amount += temp_amount
            total_amount = amount + shipping_amount
    if request.method == 'POST':
        try:
            u = request.session['id']
            p = request.POST['total_price']
            od = date.today().strftime('%Y-%m-%d')
            sd = date.today().strftime('%Y-%m-%d')
            o = request.POST['ordered']
            bill = request.POST['billing_Address']
            order = Order(user_id_id=u, total_price=p, start_date=sd, ordered_date=od, ordered=o,
                          billing_Address_id=bill)
            print("__", order)
            order.save()
            print("__", order)
            return redirect('/client/payment_done/')
        except:
            print("___", sys.exc_info())
    return render(request, 'order_summary.html', {'us': us, 'bil': bil, 'cart': cart, 'amount': amount, 'total_amount':
        total_amount})







