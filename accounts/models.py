from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Game(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class University(models.Model):
	college = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.college

class Member(models.Model):

	name = models.CharField(max_length=200, null=True, unique = True)
	#college = models.ForeignKey(University, null=True, on_delete=models.CASCADE)
	college = models.CharField(max_length=200, null=True)
	email = models.EmailField(max_length=255, null=True,unique=True)
	phone = models.CharField(max_length=200, null=True, unique = True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	@classmethod
	def create(self, name, email=None, college=None, phone=None):
		member=self(name=name, email=email, college=college,phone=phone)
		return member

	def __str__(self):
		return self.name

# class UserMember(models.Model):

# 	name = models.CharField(max_length=200, null=True)
# 	college = models.ForeignKey(University, null=True, on_delete=models.CASCADE)
# 	phone = models.CharField(max_length=200, null=True)

# 	date_created = models.DateTimeField(auto_now_add=True, null=True)

# 	def __str__(self):
# 		return self.name

class Tier(models.Model):
	TIER = (
		('Tier 1', 'Tier 1'),
		('Tier 2', 'Tier 2'),
		('Tier 3', 'Tier 3'),
		)
	member = models.ForeignKey(Member, null=True, on_delete=models.CASCADE)
	game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
	tierlist = models.CharField(max_length=200, null=True, choices=TIER)
	played = models.IntegerField(default=0)
	won = models.IntegerField(default=0, null=True)

	@classmethod
	def create(cls, member):
		tier = cls(member=member)
		return tier



class Announcement(models.Model):
	typ = models.CharField(max_length=200, null=True)
	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)

	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name