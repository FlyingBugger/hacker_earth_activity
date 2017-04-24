from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from register.models import *


def index(request):
	return render(request, "index.html")


@api_view(['POST'])
def post_message(request):
	data = request.data
	serializer = RegisterMessageSerializer(data=data)
	if serializer.is_valid():
		register_message = serializer.create(serializer.validated_data)
		return Response(RegisterMessageSerializer(register_message).data)
	return Response(serializer.errors)
