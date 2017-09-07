#coding:utf-8
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from models import *
from rest_framework.decorators import api_view
from rest_framework import status





@api_view(['POST'])
def commit(request):
	serializer=ParticipatorSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		result = {
			'status': 200,
			'msg': '恭喜您报名成功！',
			'data': '',
		}
		return JsonResponse(result)
	return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
