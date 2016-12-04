from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Requester, Supervisor, Application, UserType
from .forms import ApplicationForm

# Create your views here.

@login_required
def requester_dashboard(request, userid):
	application_list = Application.objects.filter(requester_id=userid).order_by('-create_date')
	context = {
		'application_list': application_list,
	}
	return render(request, 'applications/requester_dashboard.html', context)

def create_application(request, userid):
	form = ApplicationForm(request.POST)
	if form.is_valid():
		advance_amount = form.cleaned_data['advance_amount']
		total_amount_requested = form.cleaned_data['total_amount_requested']
		