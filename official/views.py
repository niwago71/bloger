

from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from django.contrib.sessions.models import Session
from django.shortcuts import render,redirect
from django.contrib import auth
import datetime as dt
import os 
import random 
from .models import *
# Create your views here.

def index(response):
    return render(response,"main/index.html")
