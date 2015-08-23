from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.crypto import get_random_string
from django.db.models import Max

from .models import OTH, UserOTHStatus, Question
from .forms import CreateOTHForm, AddQuestionToOTHForm

def home(request):
	context = {}

	oth_list = OTH.objects.filter(completed=False)
	context['active_oths'] = [(i.oth_id, i.title) for i in oth_list]

	if request.user.is_authenticated():
		context['logged_in'] = True
		context['username'] = request.user.username
	else:
		context['logged_in'] = False

	return render(request,'index.html',context)


def logout_user(request):
	logout(request)

	return redirect('home')

@permission_required('is_staff')
@login_required(login_url='login')
def create(request):
	context = {}

	if request.user.is_authenticated():
		context['logged_in'] = True
		context['username'] = request.user.username
	else:
		context['logged_in'] = False

	if request.method == "GET":
		form = CreateOTHForm()

		context['form'] = form

	elif request.method == "POST":
		form = CreateOTHForm(request.POST)

		if form.is_valid():
			form_data = form.cleaned_data

			title = form_data['title']
			duration = form_data['duration']
			oth_id = get_random_string(length=5)

			OTH.objects.create(oth_id=oth_id, title=title, duration=duration)

			context['messageclass'] = 'success'
			context['oth_id'] = oth_id

	return render(request,'create_oth.html',context)

@permission_required('is_staff')
@login_required(login_url='login')
def add_question_to_oth(request,oth_id):
	context = {}

	oth = OTH.objects.get(oth_id=oth_id)

	level = oth.question_set.aggregate(Max('level'))['level__max']+ 1

	if request.user.is_authenticated():
		context['logged_in'] = True
		context['username'] = request.user.username
	else:
		context['logged_in'] = False

	if request.method == "GET":
		form = AddQuestionToOTHForm(initial={'oth_id':oth_id,'level':level})

		context['form'] = form
		context['oth_title'] = oth.title
		context['oth_id'] = oth_id

	elif request.method == "POST":
		form = AddQuestionToOTHForm(request.POST,request.FILES)
		if form.is_valid():
			form_data = form.cleaned_data

			question_text = form_data['question_text']
			level = form_data['level']



	return render(request,'add_question.html',context)

@login_required(login_url='login')
def view_oth_question(request,oth_id,question_id):
	context = {}

	if request.user.is_authenticated():
		context['logged_in'] = True
		context['username'] = request.user.username
	else:
		context['logged_in'] = False

	oth = OTH.objects.get(oth_id=oth_id)
	question = Question.objects.get(question_id=question_id)

	if request.method == "GET":
		form = SubmitAnswerForm()

	elif request.method == "POST":
		form = SubmitAnswerForm(request.POST)

		if form.is_valid():
			form_data = form.cleaned_data

			answer = form_data['answer']

			if question.answer.strip() == answer.strip():
				pass
	

@login_required(login_url='login')
def view_oth(request,oth_id):
	context = {}

	if request.user.is_authenticated():
		context['logged_in'] = True
		context['username'] = request.user.username
	else:
		context['logged_in'] = False

	oth = OTH.objects.get(oth_id=oth_id)

	if oth:
		context['messageclass'] = 'success'
		context['oth_title'] = oth.title
		context['oth_id'] = oth.oth_id
		context['q_id'] = oth.question_set.filter(level=1)[0].question_id

	else:
		context['messageclass'] = 'error'
		context['message'] = "That doesn't seem to be a valid OTH id. Try again later."


	return render(request,'view_oth.html',context)

@login_required(login_url='login')
def leaderboard(request,oth_id):
	context = {}

	if request.user.is_authenticated():
		context['logged_in'] = True
		context['username'] = request.user.username
	else:
		context['logged_in'] = False

	oth_queryset = UserOTHStatus.objects.filter(oth__oth_id=oth_id)

	if oth_queryset:
		leaderboard_queryset = oth_queryset.order_by('-level','updated_at')
		context['messageclass'] = 'success'
		context['oth_title'] = leaderboard_queryset[0].oth.title
		context['entries'] = [(i+1,(j.user.username, j.level, j.updated_at))
			for i,j in enumerate(leaderboard_queryset)]
	else:
		context['messageclass'] = 'error'
		context['message'] = "That doesn't seem to be a valid OTH id. Try again later."

	return render(request,'leaderboard.html',context)
