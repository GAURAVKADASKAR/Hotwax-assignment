# Generated by Django 5.1 on 2024-12-28 05:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('size', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMech',
            fields=[
                ('contact_mech_id', models.AutoField(primary_key=True, serialize=False)),
                ('street_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHeader',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('billing_contact_mech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='billing_orders', to='home.contactmech')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer')),
                ('shipping_contact_mech', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_orders', to='home.contactmech')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_seq_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(max_length=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.orderheader')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
