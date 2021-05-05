# Generated by Django 3.1 on 2021-05-02 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VueloFactura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(max_length=10)),
                ('comida', models.SmallIntegerField()),
                ('bebida', models.SmallIntegerField()),
                ('pelicula', models.SmallIntegerField()),
                ('servicios', models.SmallIntegerField()),
                ('subtotal', models.FloatField()),
                ('descuentoM', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
    ]
