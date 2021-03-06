# Generated by Django 4.0.1 on 2022-01-13 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('descrip', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('tom', models.IntegerField()),
                ('genre', models.CharField(choices=[('Detective', 'Detective'), ('Fantasty', 'Fantasty'), ('Horror', 'Horror'), ('Dramma', 'Dramma'), ('FairyTales', 'FairyTales')], max_length=100)),
                ('date_write', models.DateField()),
            ],
        ),
    ]
