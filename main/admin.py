from django.contrib import admin
from .models import UserOTHStatus, Question, OTH

admin.site.register(UserOTHStatus)
admin.site.register(OTH)
admin.site.register(Question)