from django.db import models

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
    