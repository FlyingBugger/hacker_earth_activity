# coding=utf-8
import os
import sys
import requests
from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
from register.models import *
from sign import *
from django.http import JsonResponse


APPID=os.getenv("MONSTAR_WECHAT_PUBLIC_APPID")
APPSECRET=os.getenv("MONSTAR_WECHAT_PUBLIC_APPSECRET")
temp_token_url="https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
temp_ticket_url="https://api.weixin.qq.com/cgi-bin/ticket/getticket?type=jsapi&access_token={}"
JSAPI_ticket=""





@require_POST
def get_wexin_params(request):
	share_url=request.POST.get("share_url")
	WEXIN_PARAMS = GetWexinParams (JSAPI_ticket, share_url)
	return JsonResponse(WEXIN_PARAMS)


def GetWexinParams(ticket,share_url):

	if 0:
		temp_sign = Sign (ticket,share_url).sign ()
	else:
		token_url=temp_token_url.format(APPID,APPSECRET)
		token_json=requests.get(token_url).json()
		print token_json
		access_token=token_json["access_token"]

		ticket_url=temp_ticket_url.format(access_token)
		ticket_json=requests.get(ticket_url).json()
		ticket=ticket_json["ticket"]
		expires_in=ticket_json["expires_in"]
		global temp_ticket
		temp_ticket=ticket
		sign_json=Sign(ticket,share_url).sign()
	return sign_json


def getMP_varify(request):
	return HttpResponse ("XWsldS5dzRvbRcvT")


def index(request):
	return render (request, "moc/index.html")

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
