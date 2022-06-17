from django.contrib.auth.models import User
from django.db import models
from django.core.validators import FileExtensionValidator, MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.


class IceCreamCategory(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Header",
        verbose_name="Header:",
        help_text='<small class="text-muted">this is our header</small><hr><br>',

        max_length=250,
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('title',)
        verbose_name = 'Category'
        verbose_name_plural = 'IceCream Category'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.title}'


class IceCreamIngredient(models.Model):
    name = models.TextField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Name",
        verbose_name="Name:",
        help_text='<small class="text-muted">name of an ice-cream</small><hr><br>',
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('name',)
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.name}'


class IceCream(models.Model):
    title = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Header",
        verbose_name="Header:",
        help_text='<small class="text-muted">this is our header</small><hr><br>',

        max_length=250,
    )
    image = models.ImageField(
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="img/receipt/default/default_receipt.jpg",
        verbose_name="Image:",
        help_text='<small class="text-muted">this is our image</small><hr><br>',

        validators=[FileExtensionValidator(['jpg', 'png'])],
        upload_to='img/receipt',
        max_length=100,
    )
    time_to_cook = models.IntegerField(  # BigIntegerField SmallIntegerField PositiveIntegerField ...
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="1",
        verbose_name="Time needed(in minuts)",
        help_text='<small class="text-muted">this is the time needed</small><hr><br>',

        validators=[MinValueValidator(1), MaxValueValidator(9999)],
    )
    category = models.ManyToManyField(
        db_column='country_db_column',
        db_index=True,
        db_tablespace='country_db_tablespace',
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        default=None,
        verbose_name='IceCream Category',
        help_text='<small class="text-muted">Category</small><hr><br>',

        to=IceCreamCategory,
    )
    author = models.ForeignKey(
        db_index=True,
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='Author of an IceCream',
        help_text='<small class="text-muted">Author</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,  # CASCADE - удаляет всю запись, при удалении связанной записи
        # SET_NULL - зануляет всю запись, при удалении связанной записи DO_NOTHING - ничего не делать
    )
    ingredients = models.ManyToManyField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        default=None,
        verbose_name='IceCream Ingredients',
        help_text='<small class="text-muted">Ingredients</small><hr><br>',

        to=IceCreamIngredient,
    )

    description = models.TextField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=False,
        null=False,
        default="Description",
        verbose_name="Description:",
        help_text='<small class="text-muted">this is our description</small><hr><br>',
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('title', 'description')
        verbose_name = 'IceCream'
        verbose_name_plural = 'IceCream'

    def __str__(self):  # возвращает строковое представление объекта
        return f'{self.title}'
        


class IceCreamComment(models.Model):
    comment_text = models.CharField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="Comment",
        verbose_name="Header:",
        help_text='<small class="text-muted">Comment here</small><hr><br>',

        max_length=500,
    )
    user = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='User',
        help_text='<small class="text-muted">User</small><hr><br>',

        to=User,
        on_delete=models.SET_NULL,  # CASCADE SET_NULL DO_NOTHING
    )
    IceCream = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='IceCream',
        help_text='<small class="text-muted">Рецепт</small><hr><br>',

        to=IceCream,
        on_delete=models.CASCADE,  # CASCADE SET_NULL DO_NOTHING
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('comment_text', )
        verbose_name = 'IceCream Comment'
        verbose_name_plural = 'Comment IceCreams'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.comment_text[:10:1]}'

class IceCreamRating(models.Model):
    is_liked = models.BooleanField(
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=False,
        verbose_name="Like:",
        help_text='<small class="text-muted">Like</small><hr><br>',
    )
    rating_value = models.IntegerField(  # BigIntegerField SmallIntegerField PositiveIntegerField ...
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default="0",
        verbose_name="Mark",
        help_text='<small class="text-muted">Mark</small><hr><br>',

        validators=[MinValueValidator(0), MaxValueValidator(10)],
    )
    user = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='User',
        help_text='<small class="text-muted">User</small><hr><br>',

        to=User,
        on_delete=models.CASCADE,  # CASCADE SET_NULL DO_NOTHING
    )
    IceCream = models.ForeignKey(
        error_messages=False,
        primary_key=False,
        unique_for_date=False,
        unique_for_month=False,
        unique_for_year=False,
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        verbose_name='IceCream',
        help_text='<small class="text-muted">IceCream</small><hr><br>',

        to=IceCream,
        on_delete=models.CASCADE,  # CASCADE SET_NULL DO_NOTHING
    )

    class Meta:
        app_label = 'app_student'
        ordering = ('IceCream',)
        verbose_name = 'IceCream Rate'
        verbose_name_plural = 'IceCream Rates'

    def __str__(self):  # возвращает строкове представление объекта
        return f'{self.receipt}'