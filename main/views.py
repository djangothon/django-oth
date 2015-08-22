from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string



def logout_user(request):
	logout(request)

	return redirect('login')

def create(request):

	pass

def 

