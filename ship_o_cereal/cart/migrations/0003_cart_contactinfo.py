# Generated by Django 3.2.1 on 2021-05-14 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_contactinfo_user'),
        ('cart', '0002_rename_customer_cartitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='contactinfo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='checkout.contactinfo'),
        ),
    ]
