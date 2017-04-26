#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
from rest_framework import serializers

app_label = 'register'

CAMPUS_CHOICE = [
	('s', '沙河校区'),
	('q', '清水河校区')
]
GRADES = [
	('f', '大一'),
	('sf', '大二'),
	('j', '大三'),
	('sn', '大四'),
	('m', '研究生'),
]

@python_2_unicode_compatible
class RegisterMessage(models.Model):
	name = models.CharField(max_length=30,null=False)
	phone = models.CharField(primary_key=True, max_length=11,null=False)
	email = models.EmailField(null=False)
	qq = models.CharField(max_length=12, null=True, blank=True)
	language = models.CharField(max_length=12, blank=True, null=True)
	campus = models.CharField(max_length=1, choice=CAMPUS_CHOICE)
	grade = models.CharField('年级', max_length=2, choice=GRADES)
	major = models.CharField(max_length=20)
	register_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name


class RegisterMessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisterMessage
		fields = "__all__"
