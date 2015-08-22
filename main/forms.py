from django import forms

class CreateOTHForm(forms.Form):
	title = forms.CharField(max_length=200)
	duration = forms.IntegerField(required=False,label='Duration in minutes (optional)')

class AddQuestionToOTHForm(forms.Form):
	pass