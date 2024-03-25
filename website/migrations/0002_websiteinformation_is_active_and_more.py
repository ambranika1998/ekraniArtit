# Generated by Django 5.0.2 on 2024-03-09 19:40

import django.core.validators
import website.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='websiteinformation',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Only one should be active otherwise system does not know which one is correct', verbose_name='is active'),
        ),
        migrations.AlterField(
            model_name='websitemenu',
            name='background',
            field=models.FileField(upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='background'),
        ),
        migrations.AlterField(
            model_name='websitemenu',
            name='file',
            field=models.FileField(upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='file'),
        ),
        migrations.AlterField(
            model_name='websitemenu',
            name='slogan',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan'),
        ),
        migrations.AlterField(
            model_name='websitemenu',
            name='slogan_albanian',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan albanian'),
        ),
    ]
