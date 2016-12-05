from django.forms import ModelForm, Textarea
from django import forms
from applications.models import Application

class ApplicationForm(ModelForm):

	registration_cost = forms.IntegerField(label='Registration Cost', required=True)
	transportation_cost = forms.IntegerField(label='Transportation Cost', required=True)
	accomodation_cost = forms.IntegerField(label='Acoomodation Cost', required=True)
	meals_cost = forms.IntegerField(label='Meals Cost', required=True)
	conference_name = forms.CharField(label='Conference Name', max_length=100, required=True)
	conference_website = forms.CharField(label='Conference Website', max_length=1000)
	start_date = forms.DateField(label='Start Date', required=True)
	end_date = forms.DateField(label='End Date', required=True)

	def clean_dates(self):
		start_date = clean_data.get("start_date")
		end_date = clean_data.get("end_")
		if end_date < start_date:
			msg = u"End date should be greater than start date."
			self._errors["end_date"] = self.error_class([msg])

	class Meta:
		model = Application
		fields = ['registration_cost', 'transportation_cost', 'accomodation_cost', 'meals_cost', 'conference_name', 'conference_website', 'start_date', 'end_date']
		# widgets = {
		# 	'description': Textarea(attrs={'cols': 20, 'rows': 5})
		# }