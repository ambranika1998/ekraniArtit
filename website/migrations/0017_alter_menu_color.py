# Generated by Django 5.0.2 on 2024-03-25 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_menu_background_color_menu_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='color',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='color'),
        ),
    ]
