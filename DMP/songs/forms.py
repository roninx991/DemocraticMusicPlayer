from django import forms
from .models import Song

class SongCreateForm(forms.Form):
		Name 		= forms.CharField(required=True)
		Singer		= forms.CharField(required=False)
		Genre		= forms.CharField(required=False)
		
		def clean_name(self):
			name = self.cleaned_data.get("Name")
			if name == "Hello":
				raise forms.ValidationError("Not a valid name!")
			return name
		
class SongDetailCreateForm(forms.ModelForm):
		
		class Meta:
			model = Song
			fields = [
				'Name',
				'Singer',
				'Genre',
			]
		def clean_Name(self):
			Name = self.cleaned_data.get("Name")
			if Name == "Hello":
				raise forms.ValidationError("Not a valid name!")
			return Name

