# Generated by Django 5.0.6 on 2024-05-19 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bukapp', '0002_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='book',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]