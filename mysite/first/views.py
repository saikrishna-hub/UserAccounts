from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Register
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.contrib import auth
from django.db.models import constraints
from django.db import IntegrityError

# Create your views here.

def index(request):
    if request.method == "POST":
           username = request.POST["username"]
           firstname = request.POST["first_name"]
           lastname = request.POST["last_name"]
           email = request.POST["email"]
           password = request.POST["password"]
           hobbies = request.POST["hobbies"]

           user1 = Register(username=username, firstname=firstname, lastname=lastname, email=email, password=password, hobbies=hobbies)
           try:
                user1.save()
                return redirect("login")
           except IntegrityError as e:
               if "first_register_username_key" in str(e.args):
                   messages.info(request, "username exist")
                   return redirect("index")
               elif "first_register_email_key" in str(e.args):
                   messages.info(request, "email exist")
                   return redirect("index")


    else:
        return render(request, "first/index.html")

def login(request):
    if request.method == "POST":
                username = request.POST["username"]
                password = request.POST["password"]
                try:
                    check = Register.objects.get(username=username)
                    if username == check.username:
                        if password == check.password:

                            #auth.authenticate(username)
                            username = check.username
                            firstname = check.firstname
                            lastname = check.lastname
                            email = check.email
                            password = check.password
                            hobbies = check.hobbies
                            return render(request, "first/detail.html", {"username" : username, "firstname": firstname, "lastname" : lastname, "email" : email, "hobbies":hobbies})
                        else:
                            messages.info(request, "Please enter correct password")
                            return redirect("login")

                    else:
                        messages.info(request, "Username doesnot exist")
                        return redirect("login")
                except Register.DoesNotExist:
                    messages.info(request, "User doesn't exist")
                    return redirect("login")

    else:
       return render(request, "first/login.html")

def detail(request):
    if request.method == "POST":
        username = request.POST["username"]
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        hobbies = request.POST["hobbies"]
        users = Register.objects.get(username=username)
        users.username = username
        users.firstname = firstname
        users.lastname = lastname
        users.email = email
        users.hobbies = hobbies
        users.save()
        d = messages.info(request, "Changes updated")
        return redirect("detail")

    else:

        return render(request, "first/detail.html")

