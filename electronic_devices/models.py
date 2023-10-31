from django.db import models


NULLABLE = {
    'null': True,
    'blank': True
}


class Supplier(models.Model):
    """
    Модель поставщика
    """
    name = models.CharField(max_length=250, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=250, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=200, verbose_name='Номер дома', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    """
    Модель продукта
    """
    name = models.CharField(max_length=250, verbose_name='Название')
    model = models.CharField(max_length=250, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода продукта на рынок')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Долг')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class NetworkNode(models.Model):
    """
    Модель сети
    """
    NODE_TYPES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )
    name = models.CharField(max_length=250, verbose_name='Название')
    level = models.IntegerField(choices=NODE_TYPES, verbose_name='Уровень сети')
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    street = models.CharField(max_length=250, verbose_name='Улица', **NULLABLE)
    house_number = models.CharField(max_length=200, verbose_name='Номер дома', **NULLABLE)
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сеть'
        verbose_name_plural = 'Сети'
