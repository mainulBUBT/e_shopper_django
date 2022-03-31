from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from apps.models import Brand, Category, Contact, Order, Product, UserForm, Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.contrib.auth.models import User


def index(request):
    category = Category.objects.all()
    brand = Brand.objects.all()

    brandID = request.GET.get('brand')
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    elif brandID:
        product = Product.objects.filter(brand=brandID).order_by('-id')
    else:
        product = Product.objects.all()

    dictn = {'category': category, 'product':product, 'brand':brand}
    return render(request, 'index.html', context=dictn) 

def register(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            print
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1']
            )
            login(request, user)
            messages.info(request, 'Account Created!', extra_tags='success')
            return redirect('register')
    else:
        form = UserForm()
    
    dictn = {'form': form }
    return render(request, 'registration/register.html', context=dictn)

def contact_page(request):
    if request.method == "POST":
        contact = Contact(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
        )
        contact.save()
    return render(request, "contact.html")


def checkout(request):
    if request.method == "POST":
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        pincode = request.POST.get("address")
        cart = request.session.get("cart")
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)

        for i in cart:
            order = Order(
                user = user,
                image=cart[i]["image"],
                product = cart[i]["name"],
                price = cart[i]["price"],
                quantity = cart[i]["quantity"],
                phone = phone,
                address = address,
                pincode = pincode,
                total = (int(cart[i]["price"]))*(cart[i]["quantity"])
            )
            order.save()
        request.session['cart'] = {}
        return redirect("index")
    return HttpResponse("This is Checkout Page")

def your_order(request):
    uid = request.session.get("_auth_user_id")
    user = User.objects.get(pk=uid)
    
    order = Order.objects.filter(user=user)

    return render(request, 'order.html', context={'order':order})


#CART FUNCTIONALITIES BELOW
@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')