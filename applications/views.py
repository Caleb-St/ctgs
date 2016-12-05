from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Requester, Supervisor, Application, UserType
from .forms import ApplicationForm

from datetime import datetime

# Create your views here.

@login_required
def requester_dashboard(request, id):
	requester = request.user
	application_list = Application.objects.filter(requester_id=requester.id).order_by('-create_date')
	context = {
		'application_list': application_list,
		'empty_message': 'You currently have no grant applications.',
		'user_id': user_id,
	}
	return render(request, 'applications/requester_dashboard.html', context)

@login_required
def supervisor_dashboard(request, user_id):
	context = {
		'no_pending_applications': 'There are currently no applications needing your recommendation.',
		'no_applications': 'None of your students have submitted applications yet.',
	}
	return render(request, 'applications/supervisor_dashboard.html', context)

def create_application(request, userid):
	form = ApplicationForm(request.POST)
	if form.is_valid():
		requester = request.user
		cost_registration = form.cleaned_data['registration']
		cost_transportation = form.cleaned_data['transportation']
		cost_accomodation = form.cleaned_data['accomodation']
		cost_meal = form.cleaned_data['meals']
		description = form.cleaned_data['description']

		conference_name = form.cleaned_data['conference_name']
		conference_website = form.cleaned_data['conference_website']
		
		
		application = Application()
		application.requester = requester
		application.cost_registration = cost_registration
		application.cost_transportation = cost_transportation
		application.cost_accomodation = cost_accomodation
		application.cost_meal = cost_meal
		application.description = description
		application.save()

		return HttpResponseRedirect(reverse('applications:create_applicaiton', args=(requester.id)))

	context = {
		'form': form
	}
	return (request, 'applications/requester_dashboard.html', context)

@login_required
def make_recommendation(request):
	supervisor = request.user
	context = {
	}
	render(request, 'applications/supervisor_dashboard.html', context)