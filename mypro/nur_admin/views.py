from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from .form import ProForm
from .function import handle_uploaded_file
from .models import Nursery, customer


def dashboard(request):
    return render(request, 'index.html')

def admin_login(request):
    return render(request, 'admin_login.html')


def insert_pro(request):
    if request.method == "POST":
        p = ProForm(request.POST, request.FILES)
        print("__", p)
        if p.is_valid():
            try:
                handle_uploaded_file(request.FILES['file'])
                p.save()
                print("___", p)
                return redirect('/table_pro/')
            except:
                pass
    else:
        p = ProForm()
    return render(request,'add_pro.html',{'p':p})

def table_pro(request):
    a = Nursery.objects.all()
    return render(request,"table_pro.html",{'a':a})

def edit_pro(request, id):
    s = Nursery.objects.get(id=id)
    return render(request, 'edit_pro.html', {'s':s})

def update(request, id):
    s = Nursery.objects.get(id=id)
    if request.method == 'POST':
        form = ProForm(request.POST,request.FILES, instance=s)
        try:
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                form.save()
                return redirect('/table_pro/')
        except:
            pass
    return render(request,'edit_pro.html', {'s': s})

def destroy(request, id):
    e = Nursery.objects.get(id=id)
    e.delete()
    return redirect('/table_pro/')

def admin_login(request):
    if request.method == 'POST':
        e = request.POST.get('email')
        p = request.POST.get('password')

        val = customer.objects.filter(email=e, password=p, is_admin=1).count()

        if val == 1:
            data = customer.objects.filter(email=e, password=p)
            for items in data:
                request.session['email'] = items.email
                request.session['id'] = items.id
                return redirect('/dashboard/')

        else:
            messages.error(request, 'Invalid e-mail and password')
        return render(request, 'admin_login.html')
    else:
        return render(request, 'admin_login.html')

