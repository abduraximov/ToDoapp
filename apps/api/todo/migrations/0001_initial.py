# Generated by Django 4.2.3 on 2023-07-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=128)),
                ('title_uz', models.CharField(max_length=128, null=True)),
                ('title_en', models.CharField(max_length=128, null=True)),
                ('title_ru', models.CharField(max_length=128, null=True)),
                ('slug', models.SlugField(max_length=128, unique=True)),
                ('desc', models.CharField(max_length=128)),
                ('desc_uz', models.CharField(max_length=128, null=True)),
                ('desc_en', models.CharField(max_length=128, null=True)),
                ('desc_ru', models.CharField(max_length=128, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]