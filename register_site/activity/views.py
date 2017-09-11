# coding=utf-8
import os
import sys
import requests
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
from register.models import *
from sign import *

temp_ticket=""

def GetWexinParams(p_ticket,full_url):

	if 0:
		temp_sign = Sign (p_ticket,full_url).sign ()
		print "++++"
	else:
		url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(os.getenv("HE_WECHAT_PUBLIC_APPID"),os.getenv("HE_WECHAT_PUBLIC_APPSECRET"))
		temp=requests.get(url)
		json=temp.json()
		access_token=json["access_token"]
		expires_in=json["expires_in"]
		url="https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token={}".format(access_token)
		temp=requests.get(url)
		json=temp.json()
		ticket=json["ticket"]
		global temp_ticket
		temp_ticket=ticket
		temp_sign=Sign(ticket,full_url).sign()
		print "-------{}".format(temp_sign)
	return temp_sign



def index(request):
	host=request.get_host()
	full_url=request.get_full_path()
	url=host+full_url
	print full_url
	WEXIN_PARAMS = GetWexinParams (temp_ticket,url)
	return render (request, "moc/index.html",WEXIN_PARAMS)

def get_form(request):
	return render (request, "moc/form.html")


def problems_page(request):
	return render(request, 'problems.html')


def poster_page(request):
	return render(request, "index.html")


def signup_page(request):
	return render(request, "signup.html")


@api_view(['POST'])
def post_message(request):
	data = request.data
	import json
	print json.dumps(data, indent=2)
	serializer = RegisterMessageSerializer(data=data)
	if serializer.is_valid():
		try:
			register_message = serializer.create(serializer.validated_data)
		except ValidationError, e:
			return Response(u"报名人数过多", status=status.HTTP_400_BAD_REQUEST)
		return Response(RegisterMessageSerializer(register_message).data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_certificate(request, code):
	for winner in Winner.objects.all():
		if code == winner.code:
			certificate = winner.certificate
			file_name = certificate.name
			path = os.path.join(settings.MEDIA_ROOT, file_name)
			with open(path) as pdf:
				response = HttpResponse(pdf.read(), content_type='application/pdf')
				response['Content-Disposition'] = u'filename={}_certificate.pdf'.format(winner.name)
				return response
	return HttpResponseNotFound()
