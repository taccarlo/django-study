# Generated by Django 4.2 on 2024-05-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriptiondata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_sub', models.CharField(max_length=200)),
                ('ID_prod', models.CharField(max_length=200)),
                ('prod_desc', models.CharField(max_length=500)),
                ('price', models.FloatField()),
            ],
        ),
    ]