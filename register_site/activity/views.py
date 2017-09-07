# coding=utf-8
import os
import sys

from django.http.response import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from register.models import *


def index(request):
	return render (request, "index.html")


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
