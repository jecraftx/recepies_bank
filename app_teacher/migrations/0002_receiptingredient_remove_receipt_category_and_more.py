# Generated by Django 4.0.4 on 2022-06-08 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='Название', help_text='<small class="text-muted">это наше название</small><hr><br>', null=True, verbose_name='Название:')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='receipt',
            name='category',
        ),
        migrations.AddField(
            model_name='receipt',
            name='category',
            field=models.ManyToManyField(blank=True, db_column='country_db_column', db_index=True, db_tablespace='country_db_tablespace', default=None, error_messages=False, help_text='<small class="text-muted">категория</small><hr><br>', to='app_teacher.receiptcategory', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Категория блюда'),
        ),
        migrations.AlterField(
            model_name='receiptcomment',
            name='receipt',
            field=models.ForeignKey(blank=True, default=None, error_messages=False, help_text='<small class="text-muted">Рецепт</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to='app_teacher.receipt', unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='receiptrating',
            name='user',
            field=models.ForeignKey(blank=True, default=None, error_messages=False, help_text='<small class="text-muted">Пользователь</small><hr><br>', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique_for_date=False, unique_for_month=False, unique_for_year=False, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='receipt',
            name='ingredients',
            field=models.ManyToManyField(blank=True, default=None, help_text='<small class="text-muted">ингредиенты</small><hr><br>', to='app_teacher.receiptingredient', verbose_name='Ингредиенты блюда'),
        ),
    ]
