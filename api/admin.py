from django.contrib import admin

from .models import *


@admin.register(AboutMeInformation)
class AboutMeInformation(admin.ModelAdmin):
    pass


@admin.register(Skill)
class Skill(admin.ModelAdmin):
    pass


@admin.register(Work)
class Work(admin.ModelAdmin):
    pass


@admin.register(Contact)
class Contact(admin.ModelAdmin):
    pass
