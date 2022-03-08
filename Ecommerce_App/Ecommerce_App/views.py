from django.shortcuts import render
from apps.models import Category, Product

def index(request):
    category = Category.objects.all()
    
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.objects.filter(sub_category=categoryID)
    else:
        product = Product.objects.all()

    dictn = {'category': category, 'product':product}
    return render(request, 'index.html', context=dictn) 