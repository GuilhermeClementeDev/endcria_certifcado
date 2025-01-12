# Generated by Django 5.1.4 on 2025-01-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadet', '0002_alter_cadet_created_at_alter_cadet_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadet',
            name='role_id',
        ),
        migrations.AddField(
            model_name='cadet',
            name='role_id',
            field=models.ManyToManyField(to='cadet.roles'),
        ),
    ]
