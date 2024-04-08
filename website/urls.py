from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('upcoming', views.upcoming, name='upcoming'),
    path('talks_masterclass', views.talks_masterclass, name='talks_masterclass'),
    path('schedule', views.schedule, name='schedule'),
    path('tickets', views.tickets, name='tickets'),
    path('education', views.education, name='education'),
    path('location', views.location, name='location'),
    path('archive', views.archive, name='archive'),
    path('programme', views.programme, name='programme'),
]
