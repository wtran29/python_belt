# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt, re
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9+._-]+@[a-zA-Z0-9+._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[A-Za-z]\w+$')
# Create your models here.

class UserManager(models.Manager):
	def RegValid(self, postData):
		errors ={}


class User(models.Model):
	email= models.EmailField(unique=True)


	objects = UserManager()
	
	def __str__(self):
		return self.email
