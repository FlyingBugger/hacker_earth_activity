from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(RegisterMessage)
class RegisterMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email','grade','campus', 'team_size', 'teammate', 'register_date')

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
	list_display = ('name', 'prize')