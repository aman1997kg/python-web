# Generated by Django 4.0.4 on 2022-05-11 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, db_index=True, max_length=255, verbose_name='Блог')),
                ('content', models.TextField(blank=True, db_index=True, verbose_name='Контент')),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m/%d')),
            ],
        ),
    ]
