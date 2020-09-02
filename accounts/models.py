from django.db import models

# Create your models here.


class Game(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Member(models.Model):

	name = models.CharField(max_length=200, null=True)
	college = models.CharField(max_length=200, null=True)
	games = models.ManyToManyField(Game)
	phone = models.CharField(max_length=200, null=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name




class Announcement(models.Model):
	typ = models.CharField(max_length=200, null=True)
	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name