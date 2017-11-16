from django import forms
from .models import Song

class SongCreateForm(forms.Form):
		Name 		= forms.CharField(required=True)
		Singer		= forms.CharField(required=False)
		Genre		= forms.CharField(required=False)
		
class SongDetailCreateForm(forms.ModelForm):
	class Meta:
		model = Song
		fields = [
			'Name',
			'Singer',
			'Genre',
		]
