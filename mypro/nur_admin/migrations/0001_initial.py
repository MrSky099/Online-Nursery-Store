# Generated by Django 4.0.3 on 2022-04-02 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=12)),
                ('password', models.IntegerField()),
                ('c_password', models.IntegerField()),
                ('is_admin', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Nursery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('file', models.FileField(upload_to='')),
            ],
            options={
                'db_table': 'Nursery',
            },
        ),
    ]