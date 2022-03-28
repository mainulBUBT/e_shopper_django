
from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return f'Category name is: {self.name}'

class Sub_Category(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'Sub category is: {self.name}'
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, default='')
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, null=False, default='')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product_images')
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class UserForm(UserCreationForm):
    email = forms.EmailField(label='Email Address',required=True, error_messages={'exists':'Email already exists!'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        else:
            return user
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.email

class Order(models.Model):
    image = models.ImageField(upload_to="Ecommerce_App/order/image")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    price = models.IntegerField()
    address = models.TextField()
    phone = models.CharField(max_length=11)
    pincode = models.CharField(max_length=12)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    