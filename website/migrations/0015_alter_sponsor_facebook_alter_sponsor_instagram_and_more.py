# Generated by Django 5.0.2 on 2024-03-10 02:06

import django.core.validators
import website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_websiteinformation_rights_reserved_al'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='facebook',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='instagram',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='linkedin',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='media',
            field=models.FileField(help_text='Size 456x210', upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='media'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='slogan',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='slogan_al',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan albanian'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='twitter',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='youtube',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Youtube'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='facebook',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='instagram',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Instagram'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='linkedin',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Linkedin'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='media',
            field=models.FileField(help_text='Size 1900x1200', upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='media'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='slogan',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='slogan_al',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan albanian'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='twitter',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='youtube',
            field=models.URLField(blank=True, db_index=True, null=True, verbose_name='Youtube'),
        ),
        migrations.AlterField(
            model_name='websitemenumedia',
            name='slogan',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan'),
        ),
        migrations.AlterField(
            model_name='websitemenumedia',
            name='slogan_al',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='slogan albanian'),
        ),
    ]
