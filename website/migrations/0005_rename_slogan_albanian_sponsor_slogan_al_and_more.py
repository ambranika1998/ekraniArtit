# Generated by Django 5.0.2 on 2024-03-09 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_websitemenu_background_alter_websitemenu_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsor',
            old_name='slogan_albanian',
            new_name='slogan_al',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='description_albanian',
            new_name='description_al',
        ),
        migrations.RenameField(
            model_name='staff',
            old_name='slogan_albanian',
            new_name='slogan_al',
        ),
        migrations.RenameField(
            model_name='websitemenu',
            old_name='description_albanian',
            new_name='description_al',
        ),
        migrations.RenameField(
            model_name='websitemenu',
            old_name='slogan_albanian',
            new_name='slogan_al',
        ),
        migrations.RenameField(
            model_name='websitemenumedia',
            old_name='description_albanian',
            new_name='description_al',
        ),
        migrations.RenameField(
            model_name='websitemenumedia',
            old_name='slogan_albanian',
            new_name='slogan_al',
        ),
    ]