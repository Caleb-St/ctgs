from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Requester(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	supervisor = models.ForeignKey('Supervisor', on_delete=models.CASCADE)
	student_number = models.IntegerField(unique=True)
	#academic_unit = models.CharField(max_length=200)
	sessions_completed = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(50)])
	thesis_topic = models.CharField(max_length=300)
	bank_account_number = models.CharField(unique=True, max_length=20)
	is_eligible_for_grant = models.BooleanField(default=True)

	TYPE_OF_REQUESTER_CHOICES = (
			('M', 'Masters'),
			('P', 'PhD'),
			('F', 'Fast Track')
		)
	type_of_requester = models.CharField(max_length=1, choices=TYPE_OF_REQUESTER_CHOICES)

	class Meta:
		db_table = 'Requester'

class Supervisor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	employee_number = models.IntegerField(unique=True)
	#grant_account_number = 

	class Meta:
		db_table = 'Supervisor'

class Application(models.Model):
	requester = models.ForeignKey('Requester', on_delete=models.CASCADE)
	conference = models.ForeignKey('Conference', on_delete=models.CASCADE)
	# description = models.CharField(max_length=1000, blank=True)
	cost_registration = models.IntegerField(default=0)
	cost_transportation = models.IntegerField(default=0)
	cost_accomodation = models.IntegerField(default=0)
	cost_meals = models.IntegerField(default=0)
	#advance_amount = models.IntegerField(default=0, blank=False)
	#total_amount_requested = models.IntegerField(default=0, blank=False)
	create_date = models.DateTimeField(default=datetime.now())
	last_edited = models.DateTimeField(default=datetime.now())

	STATUS_CHOICES = (
			('R', 'Rejected'),
			('P', 'Pending Faculty Approval'),
			('C', 'Changes Requested'),
			('S', 'Submitted'),
			('I', 'Incomplete')
		)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='I')

	def total_amount(self):
		advance_amount = self.cost_registration + self.cost_transportation + self.cost_accomodation + self.cost_meals
		return advance_amount

	class Meta:
		db_table = 'Application'

# class UserType(models.Model):
# 	TYPE_OF_USER_CHOICES = (
# 			('R', 'Requester'),
# 			('S', 'Supervisor')
# 		)

# 	class Meta:
# 		db_table = 'UserType'

class Conference(models.Model):
	name = models.CharField(max_length=100)
	website = models.CharField(max_length=1000)
	start_date = models.DateField()
	end_date = models.DateField()

	class Meta:
		db_table = 'Conference'
