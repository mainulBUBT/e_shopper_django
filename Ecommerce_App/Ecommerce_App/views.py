from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect, render
from apps.models import Category, Product, UserForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    category = Category.objects.all()
    
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID).order_by('-id')
    else:
        product = Product.objects.all()

    dictn = {'category': category, 'product':product}
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
