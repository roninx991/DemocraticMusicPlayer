from django import forms

class SongCreateForm(forms.Form):
		Name 		= forms.CharField(required=False)
		Singer		= forms.CharField(required=False)
		Genre		= forms.CharField(required=False)
