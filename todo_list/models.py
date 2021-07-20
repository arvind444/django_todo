from django.db import models
import datetime
# Create your models here.

class List(models.Model):
	task = models.CharField(max_length=200)
	date_added = models.DateTimeField(default=datetime.datetime.now())
	finish = models.BooleanField(default=False)

	def date_sep(self):
		return str(self.date_added).split()[0]

	def time_sep(self):
		return str(self.date_added).split()[1]

	def __str__(self):
		return self.task+' '+str(self.finish)+' '+str(self.date_sep())+' '+str(self.time_sep())