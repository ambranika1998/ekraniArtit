import os
import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy


def document_file_directory_path(instance, filename):
    """

    :param instance:
    :param filename:
    :return:
    """
    filename, file_extension = os.path.splitext(filename)
    return os.path.join(
        instance._meta.model_name,
        str(instance.id),
        '{}{}'.format(str(uuid.uuid4()), file_extension))


def get_file_type(file_field):
    try:
        if file_field:
            file_extension = os.path.splitext(file_field.name)[1]
            if file_extension in ['.MOV', '.avi', '.mp4', '.webm', '.mkv']:
                return 'video'
            if file_extension in ['.jpg', '.png', '.svg', '.gif', '.jpeg', '.jfif', '.pjpeg', '.pjp']:
                return 'image'
        return None
    except:
        return None


# Create your models here.

class WebsiteInformation(models.Model):
    class Meta:
        verbose_name = gettext_lazy("website information")
        verbose_name_plural = gettext_lazy("website informations")
        db_table = "website_information"

    title = models.CharField(verbose_name=gettext_lazy('title'), max_length=128, blank=False, null=False)
    title_al = models.CharField(verbose_name=gettext_lazy('title albanian'), max_length=128, blank=False, null=False)
    slogan = models.CharField(verbose_name=gettext_lazy('title'), max_length=500, blank=True, null=True)
    slogan_al = models.CharField(verbose_name=gettext_lazy('title'), max_length=500, blank=True, null=True)
    description = models.CharField(verbose_name=gettext_lazy('description'), max_length=1000, blank=True, null=True)
    description_al = models.CharField(verbose_name=gettext_lazy('description albanian'), max_length=1000, blank=True, null=True)
    embed_location = models.CharField(verbose_name=gettext_lazy('embed location'), max_length=500, blank=True, null=True)
    background = models.FileField(
        verbose_name=gettext_lazy('main page background'), upload_to=document_file_directory_path,
        validators=[FileExtensionValidator(
            allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])])
    logo = models.ImageField(verbose_name=gettext_lazy('logo'), upload_to=document_file_directory_path, help_text=gettext_lazy('Size 165x40'), null=True)
    email = models.EmailField(verbose_name=gettext_lazy('email'), blank=False, null=False, unique=True)
    phone_number = models.CharField(verbose_name=gettext_lazy('phone number'), max_length=50, blank=True, null=True)
    subscribe_button = models.CharField(verbose_name=gettext_lazy("subscribe button"), max_length=128, blank=True, null=True)
    subscribe_button_al = models.CharField(verbose_name=gettext_lazy("subscribe button albanian"), max_length=128, blank=True, null=True)
    address = models.CharField(verbose_name=gettext_lazy('address'), max_length=225, blank=True, null=True)
    address_al = models.CharField(verbose_name=gettext_lazy('address albanian'), max_length=225, blank=True, null=True)
    rights_reserved = models.CharField(verbose_name=gettext_lazy('rights reserved'), max_length=225, blank=True, null=True)
    rights_reserved_al = models.CharField(verbose_name=gettext_lazy('rights reserved albanian'), max_length=225, blank=True, null=True)
    instagram = models.URLField(gettext_lazy("Instagram"), max_length=200, db_index=True, unique=True, blank=True)
    facebook = models.URLField(gettext_lazy("Facebook"), max_length=200, db_index=True, unique=True, blank=True)
    twitter = models.URLField(gettext_lazy("Twitter"), max_length=200, db_index=True, unique=True, blank=True)
    youtube = models.URLField(gettext_lazy("Youtube"), max_length=200, db_index=True, unique=True, blank=True)
    linkedin = models.URLField(gettext_lazy("Linkedin"), max_length=200, db_index=True, unique=True, blank=True)
    other_social = models.URLField(gettext_lazy("Other Social"), max_length=200, db_index=True, unique=True, blank=True)
    is_active = models.BooleanField(verbose_name=gettext_lazy('is active'), default=True, help_text=gettext_lazy('Only one should be active otherwise system does not know which one is correct'))

    def __str__(self):
        return self.title


class MenuTypeChoices(models.TextChoices):
    HOME = "index", gettext_lazy('Home')
    ABOUT = "about", gettext_lazy('About')
    NEWS = 'news', gettext_lazy('News')
    TALKS_MASTERCLASS = 'talks_masterclass', gettext_lazy('Talks and Masterclass')
    SCHEDULE = 'schedule', gettext_lazy('Schedule')
    TICKETS = 'tickets', gettext_lazy('Tickets')
    LOCATION = 'location', gettext_lazy('Location')
    EDUCATION = 'education', gettext_lazy('Education')
    ARCHIVE = 'archive', gettext_lazy('Archive')
    PRIVACY_POLICY = 'privacy_policy', gettext_lazy('Privacy Policy')
    TERMS_OF_USE = 'terms_of_use', gettext_lazy('Terms of Use')
    LEGAL = 'legal', gettext_lazy('Legal')
    STAFF = 'staff', gettext_lazy('Staff')
    SPONSOR = 'sponsor', gettext_lazy('Sponsor')


class Menu(models.Model):
    class Meta:
        verbose_name = gettext_lazy("menu")
        verbose_name_plural = gettext_lazy("menus")
        db_table = "menu"

    menu_type = models.CharField(verbose_name=gettext_lazy("menu type"), max_length=30, choices=MenuTypeChoices.choices, unique=True)
    name = models.CharField(verbose_name=gettext_lazy('name'), max_length=128, blank=False, null=False)
    name_al = models.CharField(verbose_name=gettext_lazy('name albanian'), max_length=128, blank=False, null=False)
    color = models.CharField(verbose_name=gettext_lazy('color'), max_length=7, blank=True, null=True)
    background_color = models.CharField(verbose_name=gettext_lazy('background color'), max_length=7, default='#c0c0c0')

    def __str__(self):
        return self.get_menu_type_display()


class WebsiteMenu(models.Model):
    class Meta:
        verbose_name = gettext_lazy("website menu")
        verbose_name_plural = gettext_lazy("website menus")
        db_table = "website_menu"

    name = models.CharField(verbose_name=gettext_lazy('name'), max_length=128, blank=False, null=False)
    name_al = models.CharField(verbose_name=gettext_lazy('name albanian'), max_length=128, blank=False, null=False)
    menu_type = models.CharField(verbose_name=gettext_lazy("menu type"), max_length=30, choices=MenuTypeChoices.choices, unique=True)

    sub_title = models.CharField(verbose_name=gettext_lazy("sub title"), max_length=128, blank=True, null=True)
    sub_title_al = models.CharField(verbose_name=gettext_lazy("sub title albanian"), max_length=128, blank=True, null=True)

    title = models.CharField(verbose_name=gettext_lazy("title"), max_length=128, blank=True, null=True)
    title_al = models.CharField(verbose_name=gettext_lazy("title albanian"), max_length=128, blank=True, null=True)
    slogan = models.CharField(verbose_name=gettext_lazy('slogan'), max_length=500, blank=True, null=True)
    slogan_al = models.CharField(verbose_name=gettext_lazy('slogan albanian'), max_length=500, blank=True, null=True)
    description = models.CharField(verbose_name=gettext_lazy('description'), max_length=1000, blank=True, null=True)
    description_al = models.CharField(verbose_name=gettext_lazy('description albanian'), max_length=1000, blank=True, null=True)
    button = models.CharField(verbose_name=gettext_lazy("button"), max_length=128, blank=True, null=True)
    button_al = models.CharField(verbose_name=gettext_lazy("button albanian"), max_length=128, blank=True, null=True)

    date_range = models.CharField(verbose_name=gettext_lazy("date range"), max_length=128, blank=True, null=True)
    date_range_al = models.CharField(verbose_name=gettext_lazy("date range albanian"), max_length=128, blank=True, null=True)
    background = models.FileField(
        help_text=gettext_lazy('Size 1900x1200'),
        verbose_name=gettext_lazy('background'), upload_to=document_file_directory_path, null=True, blank=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])])
    file = models.FileField(
        verbose_name=gettext_lazy('file'), upload_to=document_file_directory_path,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf'])], null=True, blank=True)

    def __str__(self):
        return self.name


class WebsiteMenuMedia(models.Model):
    class Meta:
        verbose_name = gettext_lazy("website menu media")
        verbose_name_plural = gettext_lazy("website menu media list")
        db_table = "website_menu_media"

    menu_type = models.CharField(verbose_name=gettext_lazy("menu type"), max_length=30, choices=MenuTypeChoices.choices)
    title = models.CharField(verbose_name=gettext_lazy('title'), max_length=128, blank=False, null=False)
    title_al = models.CharField(verbose_name=gettext_lazy('title albanian'), max_length=128, blank=False, null=False)
    slogan = models.CharField(verbose_name=gettext_lazy('slogan'), max_length=500, blank=True, null=True)
    slogan_al = models.CharField(verbose_name=gettext_lazy('slogan albanian'), max_length=500, blank=True, null=True)
    description = models.CharField(verbose_name=gettext_lazy('description'), max_length=1500, blank=True, null=True)
    description_al = models.CharField(verbose_name=gettext_lazy('description albanian'), max_length=1500, blank=True, null=True)
    list_description = models.CharField(verbose_name=gettext_lazy('list description'), max_length=1500, blank=True, null=True, help_text='separate with "next_description"')
    list_description_al = models.CharField(verbose_name=gettext_lazy('list description albanian'), max_length=1500, blank=True, null=True, help_text='separate with "next_description"')
    is_active = models.BooleanField(verbose_name=gettext_lazy('is active'), default=True)
    media = models.FileField(
        verbose_name=gettext_lazy('main page background'), upload_to=document_file_directory_path,
        validators=[FileExtensionValidator(
            allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv', 'jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])])

    def __str__(self):
        return self.get_menu_type_display() + ' ' + self.title


class Staff(models.Model):
    class Meta:
        verbose_name = gettext_lazy("staff")
        verbose_name_plural = gettext_lazy("staffs")
        db_table = "staff"

    name = models.CharField(verbose_name=gettext_lazy('name'), max_length=128, blank=False, null=False)
    title = models.CharField(verbose_name=gettext_lazy("title"), max_length=128, blank=False, null=False)
    title_al = models.CharField(verbose_name=gettext_lazy("title albanian"), max_length=128, blank=False, null=False)
    slogan = models.CharField(verbose_name=gettext_lazy('slogan'), max_length=500, blank=True, null=True)
    slogan_al = models.CharField(verbose_name=gettext_lazy('slogan albanian'), max_length=500, blank=True, null=True)
    description = models.CharField(verbose_name=gettext_lazy('description'), max_length=1000, blank=True, null=True)
    description_al = models.CharField(verbose_name=gettext_lazy('description albanian'), max_length=1000, blank=True, null=True)
    media = models.FileField(
        verbose_name=gettext_lazy('media'), upload_to=document_file_directory_path, help_text=gettext_lazy('Size 1900x1200'),
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])])
    instagram = models.URLField(gettext_lazy("Instagram"), max_length=200, db_index=True, null=True, blank=True)
    facebook = models.URLField(gettext_lazy("Facebook"), max_length=200, db_index=True, null=True, blank=True)
    twitter = models.URLField(gettext_lazy("Twitter"), max_length=200, db_index=True, null=True, blank=True)
    youtube = models.URLField(gettext_lazy("Youtube"), max_length=200, db_index=True, null=True, blank=True)
    linkedin = models.URLField(gettext_lazy("Linkedin"), max_length=200, db_index=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Sponsor(models.Model):
    class Meta:
        verbose_name = gettext_lazy("sponsor")
        verbose_name_plural = gettext_lazy("sponsors")
        db_table = "sponsor"

    title = models.CharField(verbose_name=gettext_lazy("title"), max_length=128, blank=False, null=False)
    title_al = models.CharField(verbose_name=gettext_lazy("title albanian"), max_length=128, blank=False, null=False)
    slogan = models.CharField(verbose_name=gettext_lazy('slogan'), max_length=500, blank=True, null=True)
    slogan_al = models.CharField(verbose_name=gettext_lazy('slogan albanian'), max_length=500, blank=True, null=True)
    media = models.FileField(
        verbose_name=gettext_lazy('media'), upload_to=document_file_directory_path, help_text=gettext_lazy('Size 456x210'),
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'png', 'svg', 'gif', 'jpeg', 'jfif', 'pjpeg', 'pjp'])])
    instagram = models.URLField(gettext_lazy("Instagram"), max_length=200, db_index=True, null=True, blank=True)
    facebook = models.URLField(gettext_lazy("Facebook"), max_length=200, db_index=True, null=True, blank=True)
    twitter = models.URLField(gettext_lazy("Twitter"), max_length=200, db_index=True, null=True, blank=True)
    youtube = models.URLField(gettext_lazy("Youtube"), max_length=200, db_index=True, null=True, blank=True)
    linkedin = models.URLField(gettext_lazy("Linkedin"), max_length=200, db_index=True, null=True, blank=True)

    def __str__(self):
        return self.title
