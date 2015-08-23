from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string

from .models import OTH, UserOTHStatus, Question
from .forms import CreateOTHForm

def home(request):

	render(request,'index.html')

def logout_user(request):
	logout(request)

	return redirect('login')

def create(request):
	context = {}

	form = CreateOTHForm()

	context['form'] = form

	return render(request,'create_oth.html',context)

def add_question_to_oth(request):

	pass

def view_oth_question(request):

	pass

def view_oth(request):

	pass

def leaderboard(request):

	pass
