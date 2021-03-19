from django.contrib import admin
from .models import Pupil, LogoGroups, Profile
# Register your models here.


class ClassPupil(admin.ModelAdmin):
    list_display = (
        'id',
        'last_name',
        'first_name',
        'date'
    )


admin.site.register(Pupil, ClassPupil)


class ClassLogoGroups(admin.ModelAdmin):
    list_display = (
        'id',
        'profile',
        'pupil'
    )


admin.site.register(LogoGroups, ClassLogoGroups)


class ClassProfile(admin.ModelAdmin):
    list_display = (
        'id',
        'last_name',
        'first_name',
        'user',
    )


admin.site.register(Profile, ClassProfile)