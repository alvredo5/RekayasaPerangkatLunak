# Generated by Django 5.0.2 on 2024-11-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produc',
            name='kategori',
            field=models.CharField(default='Umum', max_length=200),
            preserve_default=False,
        ),
    ]