# Generated by Django 4.2 on 2025-05-13 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
