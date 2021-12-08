# Generated by Django 3.2.8 on 2021-12-08 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20211208_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='picture',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='shopproduct',
            old_name='p_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='shop',
            name='retailer_id',
        ),
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='first_name',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='last_name',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='phonenumber',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='shopname',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shopproduct',
            name='source',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.DeleteModel(
            name='ShopCategory',
        ),
        migrations.AddField(
            model_name='productcategory',
            name='shop_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.shop'),
        ),
    ]