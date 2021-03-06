# Generated by Django 4.0.4 on 2022-06-10 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_teacher', '0002_receiptingredient_remove_receipt_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipt',
            name='instructions',
            field=models.FileField(blank=True, default=None, help_text='<small class="text-muted">Инструкция</small><hr><br>', null=True, upload_to='file/pdf', validators=[django.core.validators.FileExtensionValidator(['PDF', 'XLSX'])], verbose_name='Инструкция:'),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='image',
            field=models.ImageField(blank=True, default='img/receipt/default/default_receipt.jpg', help_text='<small class="text-muted">это наша заставка</small><hr><br>', null=True, upload_to='img/receipt', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])], verbose_name='Заставка:'),
        ),
    ]
