# Generated by Django 3.1 on 2021-05-02 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tabla_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('edad', models.PositiveSmallIntegerField()),
                ('peso', models.FloatField()),
                ('altura', models.FloatField()),
            ],
        ),
    ]