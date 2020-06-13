from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse

from .models import *

context = {
		"pizzas" : Pizza.objects.all(),
		"toppings" : Topping.objects.all(),
		"subs" : Sub.objects.all(),
		"extras" : Extra.objects.all(),
		"subWithExtras" : SubWithExtra.objects.all(),
		"extraCheese" : ExtraCheese.objects.all(),
		"salads" : Salad.objects.all(),
		"pastaWithServings" : PastaWithServing.objects.all(),
		"dinnerPlatters": DinnerPlatter.objects.all()
}

def index(request):
	context['user' ]= request.user
	context['is_authenticated'] = request.user.is_authenticated
	return render(request, 'order/index.html', context)
	
def login_view(request):
	if request.method == "GET":
		return render(request, "registration/login.html")
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "registration/login.html", {"err_message": "Invalid Credentials"})

def sign_up(request):
	if request.method == "POST":
		username = request.POST['username']
		firstName = request.POST['firstname']
		lastName = request.POST['lastname']
		email = request.POST['email']
		phone = request.POST['phone']
		password = request.POST['password']
		if User.objects.filter(username=username).exists():
			return render(request, "registration/sign_up.html", {"err_message": "User already exists"})
		if User.objects.filter(email=email).exists():
			return  render(request, "registration/sign_up.html", {"err_message": "User with the given mail-id already exists"})
		if UserInfo.objects.filter(phone=phone).exists():
			return  render(request, "registration/sign_up.html", {"err_message": "User with the given phone already exists"})
		user = User.objects.create_user(username=username, email=email, password=password)
		user.first_name = firstName
		user.last_name = lastName
		user.save()
		u = UserInfo(user=user, phone=phone)
		u.save()
		login(request, user)
		return HttpResponseRedirect(reverse(index))
	return render(request, "registration/sign_up.html")

def order(request):
	if request.user.is_authenticated:
		context['user' ]= request.user
		context['is_authenticated'] = request.user.is_authenticated
		return render(request, "order/order.html", context)
	return render(request, "registration/login.html")

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))