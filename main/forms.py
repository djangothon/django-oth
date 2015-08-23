from django import forms

class CreateOTHForm(forms.Form):
	title = forms.CharField(max_length=200)
	duration = forms.IntegerField(required=False,label='Duration in minutes (optional)')

class AddQuestionToOTHForm(forms.Form):
	oth_id = forms.CharField(max_length=10,required=True)
	level = forms.IntegerField()
	question_text = forms.CharField(max_length=254,widget=forms.Textarea)
	image = forms.ImageField()
