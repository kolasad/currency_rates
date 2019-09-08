# Generated by Django 2.2.5 on 2019-09-07 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('currency', models.CharField(max_length=3)),
                ('exchange_rate', models.DecimalField(decimal_places=4, max_digits=20)),
                ('date', models.DateField()),
            ],
            options={
                'unique_together': {('date', 'currency')},
            },
        ),
    ]
