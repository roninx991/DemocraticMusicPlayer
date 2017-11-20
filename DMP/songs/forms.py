from django import forms
from .models import Song
from django.contrib.auth import get_user_model

User = get_user_model()

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

class RegisterForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
