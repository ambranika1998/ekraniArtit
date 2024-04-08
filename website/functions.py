import os
import uuid

from ekraniArtit.settings import HOST_MEDIA_ROOT
from website.models import WebsiteMenu, WebsiteInformation, get_file_type, Menu, MenuTypeChoices, Staff, Sponsor, WebsiteMenuMedia, DayDate


def get_language(request):
    language = request.GET.get('lang', '')
    if language != 'al':
        return '', 'en'
    else:
        return '_al', 'al'


def return_menu_data(request, menu_type_choice):
    language = get_language(request)

    website_menu = WebsiteMenu.objects.filter(menu_type=menu_type_choice).first()
    data = {
        'name': None,
        'sub_title': None,
        'title': None,
        'slogan': None,
        'description': None,
        'button': None,
        'date_range': None

    }
    if website_menu:
        data = {
            'name': getattr(website_menu, 'name' + language[0]),
            'sub_title': getattr(website_menu, 'sub_title' + language[0]),
            'title': getattr(website_menu, 'title' + language[0]),
            'slogan': getattr(website_menu, 'slogan' + language[0]),
            'description': getattr(website_menu, 'description' + language[0]),
            'button': getattr(website_menu, 'button' + language[0]),
            'date_range': getattr(website_menu, 'date_range' + language[0]),
        }
    data['website'] = get_website_information(request, language[0])
    data['menus'] = get_menu(request, language[0])
    if menu_type_choice == MenuTypeChoices.ABOUT:
        staff = get_staff_information(request, language[0])
        data['staff'] = staff
        sponsor = get_sponsor_information(request, language[0])
        data['sponsor'] = sponsor
    if menu_type_choice == MenuTypeChoices.PROGRAMME:
        data['programme_days'] = get_programme_data(request, language[0])
    if language[0] == '_al':
        data['location_placeholder'] = 'Vendndodhja'
        data['date_placeholder'] = 'Datë'
    else:
        data['location_placeholder'] = 'Location'
        data['date_placeholder'] = 'Date'
    data['media_list'] = get_website_media_list(request, language[0], menu_type_choice)
    data['language'] = language[1]
    return data


def get_website_information(request, language):
    data = {
        'home': 'index',
        'title': 'Ekrani i Artit' if language == '_al' else 'Art Screen',
        'slogan': '',
        'description': '',
        'embed_location': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2961.9294552943293!2d19.51390007557026!3d42.06613145362136!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x134e00feb8d93f51%3A0x8a3339b5fc79681e!2sArt%20House!5e0!3m2!1sen!2s!4v1708276846294!5m2!1sen!2s',
        'background': '',
        'logo': '',
        'email': 'example@email.al',
        'phone_number': '+355 60 000 0000',
        'subscribe_button': 'Abonohu' if language == '_al' else 'Subscribe',
        'address': '3805 Edwards Rd Cincinnati, OH 45209 USA',
        'rights_reserved': '',
        'instagram': '',
        'facebook': '',
        'twitter': '',
        'youtube': '',
        'linkedin': '',
        'other_social': '',
        'background_type': '',
        'logo_type': '',
        'secondary_color': '#399BFF'
    }

    if language == '_al':
        data['subscribe_info'] = 'Abonohu për përditësimet më të fundit'
        data['subscribe_placeholder'] = 'Vendosni adresën tuaj të emailit'
        data['do_not_share_your_data'] = '* Ne nuk e ndajmë informacionin tuaj me askënd.'
    else:
        data['subscribe_info'] = 'Subscribe For The Latest Updates'
        data['subscribe_placeholder'] = 'Enter your email address'
        data['do_not_share_your_data'] = '* We don’t share your information with anyone.'

    key_simple_data = ['embed_location', 'email', 'phone_number', 'instagram', 'facebook', 'twitter', 'youtube', 'linkedin', 'other_social', 'secondary_color']
    key_translated_data = ['title', 'slogan', 'description', 'address', 'rights_reserved', 'subscribe_button']
    key_file_data = ['background', 'logo']
    key_ignore = ['background_type', 'logo_type']

    website_information = WebsiteInformation.objects.filter(is_active=True).last()
    if website_information:
        data_from_website_information = {}
        for key, value in data.items():
            if key in key_ignore:
                continue
            elif key in key_translated_data:
                data_from_website_information[key] = getattr(website_information, key + language)
            elif key in key_file_data:
                data_from_website_information[key] = os.path.join(HOST_MEDIA_ROOT + str(getattr(website_information, key)))
                data_from_website_information[key + '_type'] = get_file_type(getattr(website_information, key))
            elif key in key_simple_data:
                data_from_website_information[key] = getattr(website_information, key)
            else:
                data_from_website_information[key] = value
        return data_from_website_information
    return data


def get_menu(request, language):
    data = {}
    menus = Menu.objects.all().order_by('order')
    for menu in menus:
        data[menu.menu_type] = {
            'display_name': getattr(menu, 'name' + language),
            'is_active': menu.menu_type in request.path_info,
            'color': menu.color,
            'background_color': menu.background_color
        }
    return data


def get_staff_information(request, language):
    data = {}

    if language == '_al':
        data['name'] = 'Stafi'
        data['sub_title'] = 'Njihuni me stafin tone'
        data['title'] = 'Stafi'
        data['description'] = ''
    else:
        data['name'] = 'Staff'
        data['sub_title'] = 'Meet our Staff'
        data['title'] = 'Staff'
        data['description'] = ''

    staff_data = Staff.objects.all().order_by('order')
    staff_list = []
    for staff in staff_data:
        staff_list.append(
            {
                'name': staff.name,
                'title': getattr(staff, 'title' + language),
                'media': os.path.join(HOST_MEDIA_ROOT + str(staff.media)),
                'instagram': staff.instagram,
                'facebook': staff.facebook,
                'twitter': staff.twitter,
                'youtube': staff.youtube,
                'linkedin': staff.linkedin,
            }
        )
    data['staff_list'] = staff_list
    return data


def get_sponsor_information(request, language):
    data = {}

    if language == '_al':
        data['title'] = 'Partnerët dhe Sponsorat'
        data['description'] = ''
    else:
        data['title'] = 'Partners and Sponsors'
        data['description'] = ''
    sponsors = Sponsor.objects.all().order_by('order')
    sponsor_list = []
    for sponsor in sponsors:
        sponsor_list.append(
            {
                'title': getattr(sponsor, 'title' + language),
                'media': os.path.join(HOST_MEDIA_ROOT + str(sponsor.media)),
            }
        )
    data['sponsor_list'] = sponsor_list
    return data


def get_website_media_list(request, language, menu_type_choice):
    website_menu_media_list = WebsiteMenuMedia.objects.filter(menu_type=menu_type_choice, is_active=True).order_by('order')
    media_list = []
    counter = 0
    for website_menu_media in website_menu_media_list:
        counter += 1
        media_list.append(
            {
                'title': getattr(website_menu_media, 'title' + language),
                'media': os.path.join(HOST_MEDIA_ROOT + str(website_menu_media.media)),
                'index': counter,
                'new_slide': counter % 6 == 0
            }
        )
    return media_list


def get_programme_data(request, language):
    programme_list = []
    counter = 0
    day_dates = DayDate.objects.all().order_by('order')
    for day_date in day_dates:
        info = {
            'day': getattr(day_date, 'day' + language),
            'date': getattr(day_date, 'date' + language),
            'programmes': [],
            'active_class': 'active' if programme_list == [] else ''
        }
        for programme in day_date.day_programmes.order_by('order'):
            day_info = {
                'id': programme.id,
                'title': getattr(programme, 'title' + language),
                'description': getattr(programme, 'description' + language),
                'time': programme.time,
                'active_class': 'active' if info['programmes'] == [] else ''
            }
            info['programmes'].append(day_info)
        programme_list.append(info)
    return programme_list
