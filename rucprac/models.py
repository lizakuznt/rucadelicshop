from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=50, verbose_name='Название')
    product_description = models.TextField(blank=True, verbose_name='Описание')
    product_price = models.FloatField(default=10, verbose_name='Цена')
    product_picture = models.ImageField(upload_to='image/%Y/%m/%d', blank=True, null=True, verbose_name="Фото")
    product_creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    product_modification_time = models.DateField(auto_now=True, verbose_name='Дата изменения')
    product_logical_deletion = models.DateField(null=True, blank=True, verbose_name='Сущестует?')

    def __str__(self):
        return f"{self.product_name}"

class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Название')
    category_description = models.TextField(blank=True, verbose_name='Описание')
    category_fk = models.ForeignKey(Product, related_name='category_product_fk', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.category_name}"

class Tag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='Название')
    tag_description = models.TextField(blank=True, verbose_name='Описание')
    tag_fk_mtm = models.ManyToManyField(Product)

    def __str__(self):
        return f"{self.tag_name}"

class Order(models.Model):
    order_unique_number = models.IntegerField(unique=True)
    order_creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    order_delivery_address = models.CharField(max_length=200, verbose_name='Адрес доставки')
    order_phone_number = models.CharField(max_length=100, verbose_name='Номер телефона')
    order_fio = models.CharField(max_length=100, verbose_name='ФИО клиента')
    order_fk = models.ManyToManyField(Product, through='OrderPosition', related_name='order_product_fk')

    def __str__(self):
        return f"Заказ {self.order_unique_number}"

class OrderPosition(models.Model):
    order_position_product_fk = models.ForeignKey(Product, related_name='order_position_product_fk', on_delete=models.CASCADE)
    order_position_order_fk = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    order_position_number_of_products_in_the_position = models.IntegerField(verbose_name='Количество товаров на позиции')
    order_position_discount_per_unit_of_goods = models.IntegerField(verbose_name='Скидка за единицу товара')

    def __str__(self):
        return f"Заказ {self.order_position_order_fk.order_unique_number} - Предмет {self.order_position_product_fk.product_name}"
