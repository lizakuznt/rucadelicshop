from django.db import models

class Product (models.Model):
     Product_Name = models.CharField(max_length=50, verbose_name='Название')
     Product_Description = models.TextField(blank=True, verbose_name='Описание')
     Product_Price = models.FloatField(default=10, verbose_name='Цена')
     Product_Picture = models.ImageField(upload_to='image/%Y/%m/%d',blank=True, null=True, verbose_name="Фото")
     Product_Creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания')
     Product_Modification_time = models.DateField(auto_now_add=True, verbose_name='Дата изменения')
     Product_Logical_deletion = models.DateField(auto_now_add=True, verbose_name='Сущестует?')
     def __str__(self):
        return f" {self.Product_Name}"
class Category (models.Model):
    Category_Name = models.CharField(max_length=50, verbose_name='Название')
    Category_Description = models.TextField(blank=True, verbose_name='Описание')
    Category_FK = models.ForeignKey(Product,related_name='Category_product_PK', on_delete=models.PROTECT)

    def __str__(self):
        return f" {self.Category_Name}"
class Tag (models.Model):
    Tag_Name = models.CharField(max_length=50, verbose_name='Название')
    Tag_Description = models.TextField(blank=True, verbose_name='Описание')
    Tag_FK_MTM = models.ManyToManyField(Product)

    def __str__(self):
        return f" {self.Tag_Name}"
class Order(models.Model):
    Order_Unique_number = models.IntegerField(unique=True)
    Order_Creation_time = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    Order_Delivery_address = models.CharField(max_length=200, verbose_name='Адрес доставки')
    Order_Phone_number = models.CharField(max_length=100, verbose_name = 'Номер телефона')
    Order_FIO = models.CharField(max_length=100, verbose_name='ФИО клиента')
    Order_FK = models.ManyToManyField(Product, through='OrderPosition', related_name='Order_product_PK')

    def __str__(self):
        return f"Заказ {self.Order_Unique_number}"
class OrderPosition(models.Model):
    OrderPosition_Product_FK = models.ForeignKey(Product, related_name='OrderPosition_product_PK', on_delete=models.CASCADE)
    OrderPosition_Order_FK = models.ForeignKey(Order, related_name='order', on_delete = models.CASCADE)
    OrderPosition_Number_of_products_in_the_position = models.IntegerField(verbose_name='кол-во товаров на позиции')
    OrderPosition_Discount_per_unit_of_goals = models.IntegerField(verbose_name='скидка за единицу товара')

    def __str__(self):
        return f"Заказ {self.OrderPosition_Order_FK.Order_Unique_number} - Предмет {self.OrderPosition_Product_FK.Product_Name}"