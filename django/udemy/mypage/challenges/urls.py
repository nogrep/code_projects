from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_month),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenges, name="month-challenge")
]
