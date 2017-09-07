from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Participator)
class ParticipatorAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email', 'company', 'jobtitle', 'date')
	search_fields = ('name', 'phone', 'email', 'company', 'jobtitle')
	list_filter = ('date',)
