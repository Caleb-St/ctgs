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
	#stage
	#status
	#limit = 
	description = models.CharField(max_length=1000)
	advance_amount = models.IntegerField(default=0)
	total_amount_requested = models.IntegerField(default=0)
	create_date = models.DateTimeField(default=datetime.now())

	class Meta:
		db_table = 'Application'

class UserType(models.Model):
	TYPE_OF_USER_CHOICES = (
			('R', 'Requester'),
			('S', 'Supervisor')
		)

	class Meta:
		db_table = 'UserType'