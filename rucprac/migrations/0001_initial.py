# Generated by Django 4.2.6 on 2023-12-06 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Unique_number', models.IntegerField(unique=True)),
                ('Order_Creation_time', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('Order_Delivery_address', models.CharField(max_length=200, verbose_name='Адрес доставки')),
                ('Order_Phone_number', models.CharField(max_length=100, verbose_name='Номер телефона')),
                ('Order_FIO', models.CharField(max_length=100, verbose_name='ФИО клиента')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=50, verbose_name='Название')),
                ('Product_Description', models.TextField(blank=True, verbose_name='Описание')),
                ('Product_Price', models.FloatField(default=10, verbose_name='Цена')),
                ('Product_Picture', models.ImageField(blank=True, null=True, upload_to='image/%Y/%m/%d', verbose_name='Фото')),
                ('Product_Creation_time', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('Product_Modification_time', models.DateField(auto_now_add=True, verbose_name='Дата изменения')),
                ('Product_Logical_deletion', models.DateField(auto_now_add=True, verbose_name='Сущестует?')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag_Name', models.CharField(max_length=50, verbose_name='Название')),
                ('Tag_Description', models.TextField(blank=True, verbose_name='Описание')),
                ('Tag_FK_MTM', models.ManyToManyField(related_name='Tag_product_PK', to='rucprac.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderPosition_Number_of_products_in_the_position', models.IntegerField(verbose_name='кол-во товаров на позиции')),
                ('OrderPosition_Discount_per_unit_of_goals', models.IntegerField(verbose_name='скидка за единицу товара')),
                ('OrderPosition_Order_FK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='rucprac.order')),
                ('OrderPosition_Product_FK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='OrderPosition_product_PK', to='rucprac.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='Order_FK',
            field=models.ManyToManyField(related_name='Order_product_PK', through='rucprac.OrderPosition', to='rucprac.product'),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=50, verbose_name='Название')),
                ('Category_Description', models.TextField(blank=True, verbose_name='Описание')),
                ('Category_FK', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Category_product_PK', to='rucprac.product')),
            ],
        ),
    ]
