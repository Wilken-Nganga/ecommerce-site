# Generated by Django 3.2.13 on 2022-06-03 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0004_alter_order_creation_date_alter_order_ref_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
