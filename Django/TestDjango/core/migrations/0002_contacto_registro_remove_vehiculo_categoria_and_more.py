# Generated by Django 4.0.4 on 2022-06-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('rut', models.TextField(max_length=50, verbose_name='Rut')),
                ('telefono', models.TextField(max_length=50, verbose_name='Telefono')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo')),
                ('ciudad', models.CharField(max_length=50, verbose_name='Ciudad')),
                ('comentario', models.CharField(max_length=50, verbose_name='Comentarios')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.TextField(max_length=50, verbose_name='Nombre de usuario')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo')),
                ('contraseña', models.TextField(max_length=50, verbose_name='Contraseña')),
            ],
        ),
        migrations.RemoveField(
            model_name='vehiculo',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Vehiculo',
        ),
    ]