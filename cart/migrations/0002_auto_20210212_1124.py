# Generated by Django 3.1.6 on 2021-02-12 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20210210_1847'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'سفارش', 'verbose_name_plural': 'سفارشات کاربران'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'آیتم سفارشی', 'verbose_name_plural': 'آیتم های سفارشی'},
        ),
        migrations.AlterField(
            model_name='order',
            name='being_delivered',
            field=models.BooleanField(default=False, verbose_name='being_delivered'),
        ),
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='cart.OrderItem', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='سفارش شده'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(verbose_name='تاریخ سفارش'),
        ),
        migrations.AlterField(
            model_name='order',
            name='received',
            field=models.BooleanField(default=False, verbose_name='received'),
        ),
        migrations.AlterField(
            model_name='order',
            name='refund_granted',
            field=models.BooleanField(default=False, verbose_name='refund_granted'),
        ),
        migrations.AlterField(
            model_name='order',
            name='refund_requested',
            field=models.BooleanField(default=False, verbose_name='refund_requested'),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ شروع'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.book', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False, verbose_name='سفارش شده'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='تعداد'),
        ),
    ]