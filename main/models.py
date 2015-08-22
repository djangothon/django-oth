from django.db import models
from django.contrib.auth.models import User

class UserOTHStatus(models.Model):
	user = models.OneToOneField(User)
	level = models.IntegerField()
	completed = models.BooleanField(default=False)
	
	class Meta:
		verbose_name = "User OTH Status"
		verbose_name_plural = "User OTH Statuses"

	def __str__(self):
		return self.user.username + " [Level: {}]".format(self.level)

class OTH(models.Model):
	oth_id = models.CharField(max_length=10,unique=True)
	title = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	start_time = models.DateTimeField()
	duration = models.IntegerField(blank=True)
	user_oth_status = models.ForeignKey(UserOTHStatus)

	class Meta:
		verbose_name = "OTH"
		verbose_name_plural = "OTHs"

	def __str__(self):
		return OTH.title

class Question(models.Model):
	question_id = models.CharField(max_length=10,unique=True)
	level = models.IntegerField()
	text = models.TextField()
	oth = models.ForeignKey(OTH)
	question_image = models.ImageField(upload_to='/image/')

	class Meta:
		verbose_name = "Question"
		verbose_name_plural = "Questions"

	def __str__(self):
		return self.text[:200] + "..."
