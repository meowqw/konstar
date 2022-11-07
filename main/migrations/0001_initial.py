# Generated by Django 4.1.3 on 2022-11-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Имя')),
                ('phone', models.CharField(max_length=50, verbose_name='Телефон')),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
