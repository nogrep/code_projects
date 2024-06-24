from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("This works!")


def index2(request):
    return HttpResponse("This works too!")


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no meat for the entire month!"
    elif month == "febuary":
        challenge_text = "Walk for at least 20 minutes a day."
    elif month == "march":
        challenge_text = "Learn Django for at least 3 hours a day."
    else:
        challenge_text = "This month is not supported!"
    return HttpResponse(challenge_text)
