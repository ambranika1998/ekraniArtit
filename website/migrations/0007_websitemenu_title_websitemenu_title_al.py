# Generated by Django 5.0.2 on 2024-03-09 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_websitemenu_sub_title_websitemenu_sub_title_al'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitemenu',
            name='title',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='websitemenu',
            name='title_al',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='title albanian'),
        ),
    ]
