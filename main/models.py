from django.db import models
from django.contrib.auth import User

class Question(models.Model):
	question_id = models.CharField(max_length=10,unique=True)
	level = models.IntegerField()
	text = models.TextField()
	oth = models.ForeignKey(OTH)
	question_image = models.ImageField(upload_to='/image/')

class OTH(models.Model):
	oth_id = models.CharField(max_length=10,unique=True)
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	start_time = models.DateTimeField()
	duration = models.IntegerField(blank=True)
	user_oth_status = models.ForeignKey(UserOTHStatus)

class UserOTHStatus(models.Model):
	user = models.OneToOneField(User)
	level = models.IntegerField()
	completed = models.BooleanField(default=False)