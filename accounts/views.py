from django.shortcuts import render
from django.http import HttpResponse
from .models import * 

def home(request):
	members= Member.objects.all()
	return render(request,'accounts/dashboard.html', {'members' : members});

def members(request):
	return render(request,'accounts/members.html');

def profile(request, pk_test):
	member = Member.objects.get(id=pk_test)

	context = {'members': member}
	return render(request,'accounts/profile.html',context);