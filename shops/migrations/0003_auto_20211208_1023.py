# Generated by Django 3.2.8 on 2021-12-08 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20211031_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopproduct',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='shopproduct',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='shopproduct',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='shopproduct',
            name='image_4',
        ),
        migrations.AddField(
            model_name='shopproduct',
            name='barcode',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='shopproduct',
            name='photo',
            field=models.ImageField(default=None, upload_to='Shop/ShopProduct/'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ShopCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_description', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
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
    ]
