# Generated by Django 3.2.8 on 2021-12-08 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('shopname', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=15)),
                ('photo', models.ImageField(upload_to='user/shop/')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.FloatField()),
                ('price', models.BigIntegerField()),
                ('defination', models.TextField(max_length=250)),
                ('source', models.CharField(blank=True, max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='Shop/ShopProduct/')),
                ('barcode', models.CharField(blank=True, max_length=150)),
                ('category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='shops.productcategory')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='ShopCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.BigIntegerField(default=0, editable=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('mode_of_payment', models.CharField(blank=True, choices=[('MPESA', 'm-pesa'), ('CASH', 'cash'), ('SHOP-CARD', 'shop-card')], max_length=10)),
                ('cart_products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shopproduct')),
            ],
        ),
        migrations.AddField(
            model_name='productcategory',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop'),
        ),
    ]
