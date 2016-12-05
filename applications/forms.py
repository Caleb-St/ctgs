from django.forms import ModelForm, Textarea
from django import forms
from applications.models import Application

class ApplicationForm(forms.Form):
	registration_cost = forms.IntergerField(required=True)
	transportation_cost = forms.IntergerField(required=True)
	accomodation_cost = forms.IntergerField(required=True)
	meals_cost = forms.IntergerField(required=True)
	conference_name = forms.CharField(max_length=100, required=True)
	conference_website = forms.CharField(max_length=1000)
	start_date = forms.DateField(required=True)
	end_date = forms.DateField(required=True)

class ApplicationForm(ModelForm):
	class Meta:
		model = Application
		fields = ['registration', 'transportation', 'accomodation', 'meals', 'conference_name', 'conference_website', 'start_date', 'end_date', 'description']
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 5})
		}


	def clean_dates(self):
		start_date = clean_data.get("start_date")
		end_date = clean_data.get("end_")
		if end_date < start_date:
			msg = u"End date should be greater than start date."
			self._errors["end_date"] = self.error_class([msg])