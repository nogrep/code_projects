from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

monthly_challenges_by_months = {
    "january": "Eat no meat for the entire month!",
    "febuary": "Walk for at least 20 minutes a day.",
    "march": "Learn Django for at least 3 hours a day.",
    "april": "Walk for at least 20 minutes a day.",
    "may": "Walk for at least 20 minutes a day.",
    "june": "Walk for at least 20 minutes a day.",
    "july": "Walk for at least 20 minutes a day.",
    "august": "Walk for at least 20 minutes a day.",
    "september": "Walk for at least 20 minutes a day.",
    "october": "Walk for at least 20 minutes a day.",
    "november": "Walk for at least 20 minutes a day.",
    "december": "Walk for at least 20 minutes a day.",
}

def index(request):
    return HttpResponse("This works!")


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_by_months[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponse("This month is not supported!")
