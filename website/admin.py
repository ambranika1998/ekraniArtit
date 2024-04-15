from django.contrib import admin

from website.models import WebsiteInformation, WebsiteMenu, WebsiteMenuMedia, Staff, Sponsor, Menu, DayDate, DayProgrammes, Location

# Register your models here.


admin.site.register(Menu)
admin.site.register(WebsiteInformation)
admin.site.register(WebsiteMenu)
admin.site.register(WebsiteMenuMedia)
admin.site.register(Staff)
admin.site.register(Sponsor)
admin.site.register(DayDate)
admin.site.register(Location)
