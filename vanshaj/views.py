from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import json
import uuid
from .api import imp
import datetime

from .models import User, Topic, Comment, CommentForm

def index(request):
    data = imp()
    return render(request, "vanshaj/index.html", {
        "data": data["articles"]
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "vanshaj/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "vanshaj/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "vanshaj/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "vanshaj/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "vanshaj/register.html")

def topic(request, url, topic):
    form = CommentForm()
    
    try:
        article=Topic.objects.get(topic=topic)
        root_comments = Comment.objects.all().filter(topic=article, parent=None)
        print("Object Exists!")
        return render(request, "vanshaj/topic.html",{
            "topic":article.topic,
            "url":article.url,
            "form":form,
            "root_comments":root_comments 
        })
    except Topic.DoesNotExist:
        Topic.objects.create(
            topic=topic,
            url=url
        )
        print("Object Created!")
        return render(request, "vanshaj/topic.html",{
            "topic":topic,
            "url":url,
            "form":form
        })
    
    print("Something Broke?!")
    return render(request, "vanshaj/topic.html")

@login_required
def comment(request, url, topic):

    article=Topic.objects.get(topic=topic)
    if request.method == "POST":    
        form = CommentForm(request.POST)
        if form:
            Comment.objects.create(
                user = request.user,
                topic = article,
                allowed=True,
                createdTime= datetime.datetime.now(),
                content = form.data.get('comment'), 
            )
            return HttpResponseRedirect(reverse("topic",args=(url, topic,))) 
        else:
            print("Error")
            return HttpResponseRedirect(reverse("topic",args=(url, topic,)))
    else:
        print("Error")
        return HttpResponseRedirect(reverse("topic",args=(url, topic,))) 

@login_required
def reply(request, url, topic, id):
    comment=Comment.objects.get(id=id)
    article=Topic.objects.get(topic=topic)
    if request.method == "POST":    
        form = CommentForm(request.POST)
        if form:
            Comment.objects.create(
                user = request.user,
                topic = article,
                allowed=True,
                createdTime= datetime.datetime.now(),
                content = form.data.get('comment'), 
                parent=comment,
            )
            return HttpResponseRedirect(reverse("topic",args=(url, topic,))) 
        else:
            print("Error")
            return HttpResponseRedirect(reverse("topic",args=(url, topic,)))
    else:
        print("Error")
        return HttpResponseRedirect(reverse("topic",args=(url, topic,))) 
    pass

