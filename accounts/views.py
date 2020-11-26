from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from .filters import *
from django.views.decorators.csrf import csrf_exempt


def Apply(request):
	
	profile = Profile.objects.get(id = request.POST.get('profile_id'))
	profile.is_apply=True
	profile.save()
	return HttpResponseRedirect(reverse('home'))

def Approve(request):
	
	profile = Profile.objects.get(id = request.POST.get('profile_id'))
	profile.is_apply=False
	profile.is_lead=True
	profile.save()
	return HttpResponseRedirect(reverse('home'))

def Delete(request):
	
	profile = Profile.objects.get(id = request.POST.get('profile_id'))
	profile.is_apply=False
	profile.is_lead=False
	profile.save()
	return HttpResponseRedirect(reverse('home'))

def homePage(request):
	context ={'homePage':"active"}
	return render(request,'accounts/home.html', context)

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
			members = Member.objects.filter(college = request.user.profile.college)
		games = Game.objects.all()
		tournament = Tournament.objects.all()
		leads = Profile.objects.filter(is_apply=True,is_lead=False)

		q = {'members':members, 'games':games,'tournament': tournament , 'leads':leads,'home':"active"}
		return render(request,'accounts/dashboard.html', q);
	else:
		return loginPage(request=request)

def hierarchy(request):
	if (request.user.is_authenticated):
		users = User.objects.filter(is_staff=False)

		context = {'users':users, 'hierarchy':"active"}
		return render(request,'accounts/hierarchy.html', context);

def members(request):
	if(request.user.is_staff):
		members= Member.objects.all()
	else:
		members = Member.objects.filter(college = request.user.profile.college)
	context = {'members':members, 'member_page':"active"}
	return render(request,'accounts/members.html',context);

def profile(request, pk_test):
	member = Member.objects.get(id=pk_test)
	tiers = Tier.objects.all()
	myFilter = TierFilter(request.GET, queryset=tiers)
	tiers = myFilter.qs

	context = {'members': member, 'tiers':tiers, 'myFilter': myFilter, 'profile':"active"}
	return render(request,'accounts/profile.html',context);

def userprofile(request, pk_test):
	user = User.objects.get(id=pk_test)
	profile = Profile.objects.get(user=user)
	members = Member.objects.filter(college=profile.college)
	


	context = {'user': user, 'profile':profile, 'members': members, 'var':"active"}
	return render(request,'accounts/userprofile.html',context);

def updateuser(request, pk_test):
	user = User.objects.get(id=pk_test)
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			return redirect('userprofile',pk_test=pk_test)
	else:
		u_form = UserUpdateForm(instance=user)
		p_form = ProfileUpdateForm(instance=user.profile)

	context = {'user': user, 'u_form':u_form, 'p_form':p_form}
	return render(request,'accounts/updateuser.html',context);

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
	form = GamesForm()
	if request.method == 'POST':
		form = GamesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'accounts/add_game.html', context)

def newMember(request):
	profile = Profile.objects.get(user=request.user)
	college = profile.college
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


def teamlist(request):
	team = Team.objects.all()

	context={'team':team, 'teamlist':"active"}
	return render(request, 'accounts/teamlist.html', context)


def team(request,pk):
	team = Team.objects.get(id=pk)

	context={'team':team,}
	return render(request, 'accounts/team.html', context)


def addTeam(request):
	form = TeamForm()
	if request.method == 'POST':
		form = TeamForm(request.POST)
		if form.is_valid():
			form.save(request)
			return redirect('teamlist')
	context = {'form': form,}

	return render(request, 'accounts/addteam.html', context)

def addTournament(request):
	form = TournamentForm()
	if request.method == 'POST':
		form = TournamentForm(request.POST)
		if form.is_valid():
			form.save(request)
			return redirect('home')
	context = {'form': form,}

	return render(request, 'accounts/newTourn.html', context)

def Tourn(request, pk):
	tournament = Tournament.objects.get(id=pk)
	form = AddTeamForm(instance=tournament)
	if request.method == 'POST':
		form = AddTeamForm(request.POST, instance=tournament)
		if form.is_valid():
			form.save(request)
			tournament.is_add= not tournament.is_add
			tournament.save()
			return redirect('tournament',pk=tournament.id)
	context = {'tourn': tournament,'form':form}
	return render(request, 'accounts/tournament.html', context)

def AddT(request):
	
	id = request.POST.get('pk')
	tourn = Tournament.objects.get(id = id)
	tourn.is_add= not tourn.is_add
	tourn.save()
	return HttpResponseRedirect(reverse('tournament', args=[id]))

def DelTourn(request,pk):
	tourn=Tournament.objects.get(id=pk)
	if request.method == "POST":
		tourn.delete()
		return redirect('home')
	context = {}
	return render(request, 'accounts/home.html', context)