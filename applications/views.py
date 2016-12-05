from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Requester, Supervisor, Application, Conference
from .forms import ApplicationForm

from datetime import datetime

# Create your views here.

@login_required
def requester_dashboard(request, user_id):
	u = User.objects.get(id=user_id)
	requester = u.requester
	application_list = Application.objects.filter(requester_id=requester.id).order_by('-create_date')
	context = {
		'requester': requester,
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
		'user_id': user_id
	}
	return render(request, 'applications/supervisor_dashboard.html', context)

@login_required
def create_application(request, user_id):
	form = ApplicationForm(request.POST)
	if form.is_valid():
		requester = request.user
		cost_registration = form.cleaned_data['registration']
		cost_transportation = form.cleaned_data['transportation']
		cost_accomodation = form.cleaned_data['accomodation']
		cost_meal = form.cleaned_data['meals']
		#description = form.cleaned_data['description']

		conference_name = form.cleaned_data['conference_name']
		conference_website = form.cleaned_data['conference_website']
		start_date = form.cleaned_data['start_date']
		end_date = form.cleaned_data['end_date']

		conference = Conference()
		conference.name = conference_name
		conference.website = conference_website
		conference.start_date = start_date
		conference.end_date = end_date
		conference.save()
		
		application = Application()
		application.requester = requester
		application.cost_registration = cost_registration
		application.cost_transportation = cost_transportation
		application.cost_accomodation = cost_accomodation
		application.cost_meal = cost_meal
		application.status = "S"
		#application.description = description
		application.conference = conference
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