from django.forms import ModelForm, Textarea
from applications.models import Application

class ApplicationForm(ModelForm):
	class Meta:
		model = Application
		fields = ['advance_amount', 'total_amount_requested', 'description']
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 5})
		}