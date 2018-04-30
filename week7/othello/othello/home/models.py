from __future__ import unicode_literals
# from django.core.validators import int_list_validator
from django.db import models

# Create your models here.

class gamer(models.Model):
	count = models.IntegerField(null=False)
	token = models.CharField(max_length=255,null=False)
	turn = models.IntegerField(null=False)
	board = models.CharField(max_length=2000,null=False)