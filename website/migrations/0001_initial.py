# Generated by Django 5.0.2 on 2024-03-09 16:12

import django.core.validators
import website.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('title_al', models.CharField(max_length=128, verbose_name='title albanian')),
                ('slogan', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('slogan_albanian', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('media', models.FileField(help_text='Size 456x210', upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='main page background')),
                ('instagram', models.URLField(db_index=True, null=True, verbose_name='Instagram')),
                ('facebook', models.URLField(db_index=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(db_index=True, null=True, verbose_name='Twitter')),
                ('youtube', models.URLField(db_index=True, null=True, verbose_name='Youtube')),
                ('linkedin', models.URLField(db_index=True, null=True, verbose_name='Linkedin')),
            ],
            options={
                'verbose_name': 'sponsor',
                'verbose_name_plural': 'sponsors',
                'db_table': 'sponsor',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('title_al', models.CharField(max_length=128, verbose_name='title albanian')),
                ('slogan', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('slogan_albanian', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description')),
                ('description_albanian', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description albanian')),
                ('media', models.FileField(help_text='Size 1900x1200', upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='main page background')),
                ('instagram', models.URLField(db_index=True, null=True, verbose_name='Instagram')),
                ('facebook', models.URLField(db_index=True, null=True, verbose_name='Facebook')),
                ('twitter', models.URLField(db_index=True, null=True, verbose_name='Twitter')),
                ('youtube', models.URLField(db_index=True, null=True, verbose_name='Youtube')),
                ('linkedin', models.URLField(db_index=True, null=True, verbose_name='Linkedin')),
            ],
            options={
                'verbose_name': 'staff',
                'verbose_name_plural': 'staffs',
                'db_table': 'staff',
            },
        ),
        migrations.CreateModel(
            name='WebsiteInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('title_al', models.CharField(max_length=128, verbose_name='title albanian')),
                ('slogan', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('slogan_al', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description')),
                ('description_al', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description albanian')),
                ('embed_location', models.CharField(blank=True, max_length=500, null=True, verbose_name='embed location')),
                ('background', models.FileField(upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='main page background')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='phone number')),
                ('address', models.CharField(blank=True, max_length=225, null=True, verbose_name='address')),
                ('address_al', models.CharField(blank=True, max_length=225, null=True, verbose_name='address albanian')),
                ('rights_reserved', models.CharField(blank=True, max_length=225, null=True, verbose_name='rights reserved')),
                ('instagram', models.URLField(blank=True, db_index=True, unique=True, verbose_name='Instagram')),
                ('facebook', models.URLField(blank=True, db_index=True, unique=True, verbose_name='Facebook')),
                ('twitter', models.URLField(blank=True, db_index=True, unique=True, verbose_name='Twitter')),
                ('youtube', models.URLField(blank=True, db_index=True, unique=True, verbose_name='Youtube')),
                ('linkedin', models.URLField(blank=True, db_index=True, unique=True, verbose_name='Linkedin')),
                ('other_social', models.URLField(blank=True, db_index=True, unique=True, verbose_name='Other Social')),
            ],
            options={
                'verbose_name': 'website information',
                'verbose_name_plural': 'website informations',
                'db_table': 'website_information',
            },
        ),
        migrations.CreateModel(
            name='WebsiteMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='title')),
                ('name_al', models.CharField(max_length=128, verbose_name='title albanian')),
                ('menu_type', models.CharField(choices=[('home', 'Home'), ('about', 'About'), ('news', 'News'), ('talks_masterclass', 'Talks and Masterclass'), ('schedule', 'Schedule'), ('tickets', 'Tickets'), ('location', 'Location'), ('education', 'Education'), ('archive', 'Archive'), ('privacy_policy', 'Privacy Policy'), ('terms_of_use', 'Terms of Use'), ('legal', 'Legal')], max_length=30, verbose_name='menu type')),
                ('slogan', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('slogan_albanian', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description')),
                ('description_albanian', models.CharField(blank=True, max_length=1000, null=True, verbose_name='description albanian')),
                ('background', models.FileField(upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='main page background')),
                ('file', models.FileField(upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='main page background')),
            ],
            options={
                'verbose_name': 'website menu',
                'verbose_name_plural': 'website menus',
                'db_table': 'website_menu',
            },
        ),
        migrations.CreateModel(
            name='WebsiteMenuMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_type', models.CharField(choices=[('home', 'Home'), ('about', 'About'), ('news', 'News'), ('talks_masterclass', 'Talks and Masterclass'), ('schedule', 'Schedule'), ('tickets', 'Tickets'), ('location', 'Location'), ('education', 'Education'), ('archive', 'Archive'), ('privacy_policy', 'Privacy Policy'), ('terms_of_use', 'Terms of Use'), ('legal', 'Legal')], max_length=30, verbose_name='menu type')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('title_al', models.CharField(max_length=128, verbose_name='title albanian')),
                ('slogan', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('slogan_albanian', models.CharField(blank=True, max_length=500, null=True, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=1500, null=True, verbose_name='description')),
                ('description_albanian', models.CharField(blank=True, max_length=1500, null=True, verbose_name='description albanian')),
                ('list_description', models.CharField(blank=True, help_text='separate with "next_description"', max_length=1500, null=True, verbose_name='list description')),
                ('list_description_al', models.CharField(blank=True, help_text='separate with "next_description"', max_length=1500, null=True, verbose_name='list description albanian')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('media', models.FileField(upload_to=website.models.document_file_directory_path, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])], verbose_name='main page background')),
            ],
            options={
                'verbose_name': 'website menu media',
                'verbose_name_plural': 'website menu media list',
                'db_table': 'website_menu_media',
            },
        ),
    ]
