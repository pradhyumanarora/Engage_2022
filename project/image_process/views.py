from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from image_process.detect import getExpression
from image_process.util import *

import json


@csrf_exempt # allows the function to return a HTTP response... django problem
def expression(request):
    uri = json.loads(request.body)['image_uri']
    expression = getExpression(uri)
    return JsonResponse({"mood": expression})

@csrf_exempt # allows the function to return a HTTP response... django problem
def dummy(request):
    uri = json.loads(request.body)['image_uri']
    # expression = getExpression(uri)
    return JsonResponse({"mood": uri})


# Create your views here.
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html', {})

@csrf_exempt 
def get_emotion_from_cam(request,format=None):
    emotion = json.loads(request.body)['mood']
    links = getYouTubeLinks(emotion)
    return JsonResponse({"YTLINK": links})