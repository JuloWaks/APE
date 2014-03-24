from django import forms
from gpgsign.models import Person


class PersonForm(forms.ModelForm):
	class Meta:
		model = Person
		fields = ['name', 'finger_print']
