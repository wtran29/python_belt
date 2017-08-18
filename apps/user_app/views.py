# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
	return render(request, 'user_app/index.html')

# Create your views here.
