# Generated by Django 3.1.6 on 2021-02-07 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20210207_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='percent',
            field=models.IntegerField(verbose_name='درصد تخفیف'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
    ]
