import os

from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from ekraniArtit.settings import HOST_MEDIA_ROOT
from website.functions import return_menu_data, get_website_information
from website.models import WebsiteMenu, MenuTypeChoices, WebsiteInformation


# Create your views here.

def index(request):
    data = return_menu_data(request, MenuTypeChoices.HOME)
    return render(request, 'website/index.html', data)


def about(request):
    data = return_menu_data(request, MenuTypeChoices.ABOUT)
    return render(request, 'website/about.html', data)


def news(request):
    data = return_menu_data(request, MenuTypeChoices.NEWS)
    return render(request, 'website/news.html', data)


def upcoming(request):
    return render(request, 'website/upcoming.html')


def talks_masterclass(request):
    data = return_menu_data(request, MenuTypeChoices.TALKS_MASTERCLASS)
    return render(request, 'website/talks_masterclass.html', data)


def schedule(request):
    data = return_menu_data(request, MenuTypeChoices.SCHEDULE)
    return render(request, 'website/schedule.html', data)


def tickets(request):
    data = return_menu_data(request, MenuTypeChoices.TICKETS)
    return render(request, 'website/tickets.html', data)


def education(request):
    data = return_menu_data(request, MenuTypeChoices.EDUCATION)
    return render(request, 'website/education.html', data)


def location(request):
    data = return_menu_data(request, MenuTypeChoices.LOCATION)
    return render(request, 'website/location.html', data)


def archive(request):
    data = return_menu_data(request, MenuTypeChoices.ARCHIVE)
    return render(request, 'website/archive.html', data)


def programme(request):
    data = return_menu_data(request, MenuTypeChoices.PROGRAMME)
    return render(request, 'website/programme.html', data)


def subscribe_view(request):
    if request.method == 'POST':
        name = 'Kërkesë për abonim'
        email = request.data.get('email', None)
        message = 'Lutemi që të më abononi në newsleteri-in tuaj.'
        send_mail(
            'Kërkesë për abonim',
            message,
            'ambranika@hotmail.com',
            ['ambranika1998@gmail.com'],
            fail_silently=False,
        )
        return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def sent_email_test():
    send_mail(
        'Kërkesë për abonim',
        'Ky eshte nje test',
        'ambranika@hotmail.com',
        ['ambranika1998@gmail.com'],
        fail_silently=False,
    )
