#coding:utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
# Create your models here.




@python_2_unicode_compatible
class Participator(models.Model):
	class Meta:
		ordering = ('-date',)

	name = models.CharField (max_length=20, verbose_name='姓名')
	phone = models.CharField (max_length=11, verbose_name='电话', unique=True)
	company = models.CharField (max_length=40, verbose_name='公司')
	jobtitle = models.CharField (max_length=15, verbose_name='职位')
	email = models.EmailField (verbose_name='邮箱',blank=True,null=True)
	# status = models.CharField (max_length=10, verbose_name='状态', choices=CURRENT_STATUS, default=0)
	remark = models.TextField (max_length=200, verbose_name='备注', null=True, blank=True)
	date = models.DateTimeField (auto_now_add=True, verbose_name='时间')

	def __str__ (self):
		return self.name

class ParticipatorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Participator
		fields = ('name','phone','jobtitle','email','company')

	phone = serializers.RegexField(regex=r'^\d{8,11}$',
	validators=[
		UniqueValidator (
			queryset=Participator.objects.all (),
			message="当前电话号码已提交",
		)],
	error_messages={
		'invalid':'电话号码必须是8至11位的数字',
		'blank':'请填写你的电话号码',
	})

	def __init__ (self, *args, **kwargs):
		super (ParticipatorSerializer, self).__init__ (*args, **kwargs)
		self.fields ['name'].error_messages ['blank'] = u'请填写你的姓名'
		# self.fields ['email'].error_messages ['blank']= u'请填写你的邮箱'
		self.fields ['jobtitle'].error_messages ['blank'] = u'请填写你的职位'
		self.fields ['company'].error_messages ['blank'] = u'请填写你的公司'

