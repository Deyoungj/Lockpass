# Generated by Django 4.2.3 on 2023-07-06 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('passwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='passwords',
            options={'ordering': ('-date_added',), 'verbose_name_plural': 'passwords'},
        ),
    ]
