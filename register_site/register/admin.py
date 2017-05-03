from django.contrib import admin

# Register your models here.

from .models import RegisterMessage


@admin.register(RegisterMessage)
class RegisterMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'phone', 'email','grade','campus','register_date')


