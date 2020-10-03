from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .filters import *


# def createTier(request, pk):

# 	OrderFormSet = inlineformset_factory(University, Member, fields = ('game','tierlist','played','won'), extra=3)
# 	member = Member.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Tier.objects.none(),instance = member)
# 	#form = GameForm(initial={'member':member})
# 	if request.method == 'POST':
# 		formset = OrderFormSet(request.POST,instance = member)
# 		if formset.is_valid():
# 			formset.save()
# 			pk_test = member.id
# 			return redirect('profile',pk_test=pk_test)

	# context = {'formset':formset}
	# return render(request, 'accounts/forms.html', context)

def registerPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')

	context={'form':form}
	return render(request,'accounts/register.html', context)

def loginPage(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request,username=username, password=password)

		if user is not None:
			login(request,user)
			return redirect('/')

		else:
			messages.info(request, 'Username OR Password is incorrect')

	context={}
	return render(request,'accounts/login.html', context)

def logoutUser(request):
	logout(request=request)
	return redirect('login')


def home(request):
	if (request.user.is_authenticated):
		if(request.user.is_staff):
			members= Member.objects.all()
		else:
			members = Member.objects.filter(college = request.user.first_name)
		games = Game.objects.all()
		announcements = Announcement.objects.all()

		q = {'members':members, 'games':games, 'announcements':announcements}
		return render(request,'accounts/dashboard.html', q);
	else:
		return loginPage(request=request)

def members(request):
	if(request.user.is_staff):
		members= Member.objects.all()
	else:
		members = Member.objects.filter(college = request.user.first_name)
	context = {'members':members}
	return render(request,'accounts/members.html',context);

def profile(request, pk_test):
	member = Member.objects.get(id=pk_test)
	tiers = Tier.objects.all()

	myFilter = TierFilter(request.GET, queryset=tiers)
	tiers = myFilter.qs

	context = {'members': member, 'tiers':tiers, 'myFilter': myFilter}
	return render(request,'accounts/profile.html',context);

def createTier(request, pk):
	OrderFormSet = inlineformset_factory(Member, Tier, fields = ('game','tierlist','played','won'), extra=3)
	member = Member.objects.get(id=pk)
	formset = OrderFormSet(queryset=Tier.objects.none(),instance = member)
	#form = GameForm(initial={'member':member})
	if request.method == 'POST':
		formset = OrderFormSet(request.POST,instance = member)
		if formset.is_valid():
			formset.save()
			pk_test = member.id
			return redirect('profile',pk_test=pk_test)

	context = {'formset':formset}
	return render(request, 'accounts/forms.html', context)

def updateTier(request, pk_tier):
	tier = Tier.objects.get(id=pk_tier)
	form = GameForm(instance=tier)
	if request.method == 'POST':
		form = GameForm(request.POST, instance=tier)
		if form.is_valid():
			form.save()
			pk_test = tier.member.id
			return redirect('profile',pk_test=pk_test)

	context = {'form':form}
	return render(request, 'accounts/forms.html', context)

def deleteTier(request,pk_item):

	item=Tier.objects.get(id=pk_item)
	pk_test = item.member.id
	if request.method == "POST":
		item.delete()
		return redirect('profile',pk_test=pk_test)

	context={'item':item,'member':item.member}
	return render(request, 'accounts/delete.html', context)

def newGame(request):
	form = GameForm()
	if request.method == 'POST':
		form = GameForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_game.html', context)

def newMember(request):
	college = request.user.first_name
	form = MemberForm(initial={'college':college})
	if request.method == 'POST':
		form = MemberForm(request.POST)
		if form.is_valid():
			form.save(request)
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_member.html', context)

def deleteMember(request,pk_member):

	member=Member.objects.get(id=pk_member)
	pk_test = member.id
	if request.method == "POST":
		member.delete()
		return redirect('members')

	context={'member':member}
	return render(request, 'accounts/delete_member.html', context)