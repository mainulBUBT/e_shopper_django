# Generated by Django 4.0.3 on 2022-03-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_product_category_product_sub_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conatact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]