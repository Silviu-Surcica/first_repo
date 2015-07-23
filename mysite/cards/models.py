from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Card(models.Model):
	owner=models.ForeignKey(User)
	url=models.URLField()
	name=models.CharField(max_length=6)
	image=models.ImageField()
	media_type=models.CharField(max_length=32)
	created_at=models.DateTimeField('created at')

	def __repr__(self):
		return '<{}-{}>'.format(self.pk,self.name)

	def __str__(self):              # __unicode__ on Python 2
		return self.name