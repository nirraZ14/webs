from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseBadRequest
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from .models import User,Works,Blog,Gallery,Service,Foryou

# Create your views here.
def index(request):
    allService=Service.objects.all()
    return render(request, "main/index.html",{
        "allService":allService,
    })

def blog(request):
    allblog=Blog.objects.all().order_by('id').reverse()
    if request.method=="POST":
        user=request.user
        content=request.POST['content']
        title=request.POST['title']
        img=request.POST['blogimg']
        Url=request.POST['blogUrl']
        blog=Blog(content=content,title=title,author=user, blogimg=img, blogUrl=Url)
        blog.save()

    return render(request, "main/blog.html",{
        "allblog":allblog
    })




def about(request):
    return render(request,"main/about.html")

def service(request, id):
    listing=Service.objects.get(pk=id)
    foryoulisting=listing.foryou.all()
    return render(request, "main/service.html",{
        "listing":listing,
        "foryoulisting":foryoulisting
    })
def portfolio(request):
    allwork=Works.objects.all()
    allgallery=Gallery.objects.all()
    return render(request, "main/portfolio.html",{
        "allwork":allwork,
        "allgallery":allgallery
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
            return render(request, "main/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "main/login.html")


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
            return render(request, "main/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "main/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "main/register.html")