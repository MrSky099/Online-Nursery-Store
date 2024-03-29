# Generated by Django 4.0.3 on 2022-04-02 04:37

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nur_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Street_Address', models.CharField(max_length=100)),
                ('Apartment_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Countries', models.CharField(max_length=50)),
                ('Zip', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('E_mail', models.EmailField(max_length=254)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nur_admin.customer')),
            ],
            options={
                'db_table': 'BillingAddress',
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nur_admin.nursery')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nur_admin.customer')),
            ],
            options={
                'db_table': 'CartItem',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Street_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Apartment_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Countries', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('Zip', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('E_mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nur_admin.customer')),
            ],
            options={
                'db_table': 'ShippingAddress',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('billing_Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.billingaddress')),
                ('item', models.ManyToManyField(to='client.cartitem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nur_admin.customer')),
            ],
            options={
                'db_table': 'Order',
            },
        ),
    ]
