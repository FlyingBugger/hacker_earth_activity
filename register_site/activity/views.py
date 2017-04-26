from django.shortcuts import render
from rest_framework import response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from register.models import *


def index(request):
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
		register_message = serializer.create(serializer.validated_data)
		return Response(RegisterMessageSerializer(register_message).data)
	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
