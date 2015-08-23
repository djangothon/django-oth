import os
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

def update_image_name(instance,filename):
	path = 'images/'
	fmt = get_random_string() + "." + 		filename.split('.')[-1]
	
	return os.path.join(path,fmt)


class OTH(models.Model):
	oth_id = models.CharField(max_length=10,unique=True)
	title = models.CharField(max_length=200)
	started = models.BooleanField(default=False)
	completed = models.BooleanField(default=False)
	start_time = models.DateTimeField(null=True,blank=True)
	duration = models.IntegerField(blank=True)

	class Meta:
		verbose_name = "OTH"
		verbose_name_plural = "OTHs"

	def __str__(self):
		return self.title

	def start(self):
		started = True;
		start_time = datetime.now()

class UserOTHStatus(models.Model):
	user = models.ForeignKey(User)
	level = models.IntegerField()
	started = models.BooleanField(default=False)
	completed = models.BooleanField(default=False)
	oth = models.ForeignKey(OTH)
	
	class Meta:
		verbose_name = "User OTH Status"
		verbose_name_plural = "User OTH Statuses"

	def __str__(self):
		return self.user.username + " [Level: {}]".format(self.level)

class Question(models.Model):
	question_id = models.CharField(max_length=10,unique=True)
	level = models.IntegerField()
	text = models.TextField()
	oth = models.ForeignKey(OTH)
	question_image = models.ImageField(upload_to=update_image_name,blank=True)
	answer = models.CharField(max_length=100)

	class Meta:
		verbose_name = "Question"
		verbose_name_plural = "Questions"


	def __str__(self):
		return self.text[:100] + "..." if len(self.text)>100 else self.text
