#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import hashlib

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
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
	campus = models.CharField(max_length=1, choices=CAMPUS_CHOICE)
	grade = models.CharField('年级', max_length=2, choices=GRADES, null=True, blank=True)
	major = models.CharField(max_length=20, blank=True)
	team_size = models.IntegerField(default=1, choices=[(1, 1), (2, 2)])
	teammate = models.CharField(max_length=30, blank=True, null=True)
	teammate_phone = models.CharField(max_length=11, blank=True, null=True)
	register_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if RegisterMessage.objects.count() < settings.MAX_CAPACITY:
			super(RegisterMessage, self).save(*args, **kwargs)
			return
		raise ValidationError("数量超出最大限制, 创建失败")

	def __str__(self):
		return self.name


class RegisterMessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisterMessage
		fields = "__all__"


@python_2_unicode_compatible
class Winner(models.Model):
	name = models.CharField(max_length=30, null=False)
	phone = models.CharField(max_length=11, null=False)
	email = models.EmailField(null=False)
	qq = models.CharField(max_length=20, null=True, blank=True)
	language = models.CharField(max_length=12, blank=True, null=True)
	campus = models.CharField(max_length=1, choices=CAMPUS_CHOICE)
	grade = models.CharField('年级', max_length=2, choices=GRADES, null=True, blank=True)
	major = models.CharField(max_length=20, blank=True)
	prize = models.CharField(max_length=1, choices=[('1', '第一名'), ('2', '第二名'), ('3', '第三名'), ('x', '效率奖')])
	certificate = models.FileField()

	def __str__(self):
		return self.name


	@property
	def code(self):
		text = self.phone + self.prize
		return hashlib.md5(text).hexdigest()[:6]