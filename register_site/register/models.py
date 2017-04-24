#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
from rest_framework import serializers

app_label = 'register'

@python_2_unicode_compatible
class RegisterMessage(models.Model):
	name=models.CharField(max_length=30,null=False)
	phone=models.CharField(primary_key=True, max_length=11,null=False)
	email=models.EmailField(null=False)
	register_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class RegisterMessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisterMessage
		fields = "__all__"
