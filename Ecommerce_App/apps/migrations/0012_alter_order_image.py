# Generated by Django 4.0.3 on 2022-03-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_alter_order_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='image',
            field=models.ImageField(upload_to='product_images'),
        ),
    ]
