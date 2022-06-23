from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from login.models import User


class Country(models.Model):
    producing_country = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    country_images = models.ImageField(null=True, blank=True, upload_to='image')
    class Meta:
        verbose_name = ('Country')
        verbose_name_plural = ("Country's")

    def __str__(self):
        return f'{self.producing_country}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'country_slug': self.slug})


class Brand(models.Model):
    model = models.CharField(max_length=30)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    brand_images = models.ImageField(null=True, blank=True, upload_to='brand')
    country = models.ForeignKey(
        "Country",
        on_delete=models.PROTECT,
        verbose_name='Country'
    )
    class Meta:
        verbose_name = ('Brand_car')
        verbose_name_plural = ("Brand_car's")

    def __str__(self):
        return f'{self.model}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'brand_slug': self.slug})


class OrderItems(models.Model):
    product = models.ForeignKey(
        "Auto",
        on_delete=models.PROTECT,
        related_name='order_items'
    )
    order = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user'
    )

    class Color(models.TextChoices):
        no_color = 'no_color', 'Цвет не выбран'
        black = 'black', 'Черный'
        red = 'red', 'Красный'
        metal = 'metal', 'Металлик'
        white = 'white', 'Белый'
        yellow = 'yellow', 'Желтый'

    class StatusChoices(models.TextChoices):
        NOT_PAID = 'not_paid', 'Не просмотрено'
        PAID = 'paid', 'Просмотрено'

    status = models.CharField(
        max_length=10,
        default=StatusChoices.NOT_PAID,
        choices=StatusChoices.choices
    )

    color = models.CharField(
        'Цвет',
        max_length=10,
        default=Color.no_color,
        choices=Color.choices
    )
    phone = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField('Дата когда нужен автомобиль')

    class Meta:
        verbose_name = _("order item")
        verbose_name_plural = _("order items")
        unique_together = (('product', 'order'),)

    def __str__(self):

        return f'Order = {self.order} | CAR - {self.product}| color - {self.get_color_display()}| status- ({self.get_status_display()}) | create {self.created_at}'


class Auto(models.Model):
    auto = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True, verbose_name="description")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    auto_images = models.ImageField(null=True, blank=True, upload_to='models')
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.PROTECT,
        verbose_name='Brand'
    )

    class Equipment(models.TextChoices):
        not_choice = 'not_choice', 'Комплектация не выбрана'
        basic = 'basic', 'Базовая'
        average = 'average', 'Средняя'
        maximum = 'maximum', 'Максимальная'

    equpment = models.CharField(
        max_length=10,
        default=Equipment.not_choice,
        choices=Equipment.choices
    )
    years = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ('Auto')
        verbose_name_plural = ('Auto')

    def __str__(self):
        return f'{self.brand} | {self.auto} |years| {self.years}| Equipment | {self.get_equpment_display()}'

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug': self.slug})


class Review(models.Model):
    user = models.CharField('Ф.И.О', max_length=255)
    text = models.TextField('Отзыв')

    def __str__(self):
        return f'{self.user} | отзыв {self.text}'
