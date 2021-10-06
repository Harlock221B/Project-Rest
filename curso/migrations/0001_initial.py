# Generated by Django 3.2.8 on 2021-10-06 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('titulo', models.CharField(max_length=50)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('comentarios', models.TextField(default='', max_length=200)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=10)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacao', to='curso.curso')),
            ],
            options={
                'verbose_name': 'Avaliações',
                'unique_together': {('curso', 'email')},
            },
        ),
    ]
