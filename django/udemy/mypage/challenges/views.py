from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

def all_month(request):
    list_items = ""
    months = list(monthly_challenges_by_months.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges_by_months.keys())
    try:
        redirect_month = months[month - 1]
    except:
        return HttpResponseNotFound("This month is not supported!")
    redirect_path = reverse("month-challenge", args=[redirect_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenges_by_months[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This month is not supported!")
