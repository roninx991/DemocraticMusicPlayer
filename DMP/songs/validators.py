from django.core.exceptions import ValidationError

CATEGORIES = ['Pop','Dance','Contemporary','Electrohouse','Electropop']

def validate_Genre(value):
	cat = value.capitalize()
	if not value in CATEGORIES and not cat in CATEGORIES:
		raise ValidationError("Not a valid genre!")
