# Generated by Django 5.1.3 on 2024-11-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account_module", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.AddField(
            model_name="user",
            name="avatar",
            field=models.CharField(
                blank=True, max_length=12, null=True, verbose_name="نصویر آواتار"
            ),
        ),
    ]
