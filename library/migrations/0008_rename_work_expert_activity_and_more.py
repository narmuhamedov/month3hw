# Generated by Django 4.0.1 on 2022-01-24 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_expert_books'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expert',
            old_name='work',
            new_name='activity',
        ),
        migrations.RenameField(
            model_name='expert',
            old_name='desc',
            new_name='info_exp',
        ),
        migrations.RemoveField(
            model_name='expert',
            name='books',
        ),
        migrations.DeleteModel(
            name='ExpertRecomendation',
        ),
    ]
