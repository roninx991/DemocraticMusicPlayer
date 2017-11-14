from django import forms

class SongCreateForm(forms.Form):
		Name 		= forms.CharField(required=True)
		Singer		= forms.CharField(required=False)
		Genre		= forms.CharField(required=False)
