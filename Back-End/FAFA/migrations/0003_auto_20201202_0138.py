# Generated by Django 2.1.1 on 2020-12-01 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('FAFA', '0002_auto_20201202_0042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setlocation',
            old_name='user_id',
            new_name='user',
        ),
    ]
