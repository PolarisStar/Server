# Generated by Django 2.1.3 on 2018-11-30 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, upload_to='perrito_image')),
                ('nombre', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=100)),
                ('estado', models.CharField(choices=[('rescatado', 'Rescatado'), ('disponible', 'Disponible'), ('adoptado', 'Adoptado')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('admin', models.CharField(choices=[('1', 'Si'), ('0', 'No')], default='0', max_length=10)),
            ],
        ),
    ]