# Generated by Django 4.0.3 on 2022-03-31 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_order_total_alter_order_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(upload_to='Ecommerce_App/media/product_images'),
        ),
    ]
