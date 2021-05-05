# Generated by Django 3.1 on 2021-05-02 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tabla_citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechayhora', models.DateField()),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='clientes.tabla_cliente')),
            ],
        ),
    ]
