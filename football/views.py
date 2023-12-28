from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from football.forms import ClubForm, CoachForm
from football.models import Club, Coach


def index(request):
    """View function for the home page of the site."""

    num_clubs = Club.objects.count()
    num_coaches = Coach.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_clubs": num_clubs,
        "num_coaches": num_coaches,
        "num_visits": num_visits + 1,
    }

    return render(request, "football/index.html", context=context)


class ClubListView(generic.ListView):
    model = Club
    template_name = "football/club_list.html"
    context_object_name = "clubs_list"


class ClubCreateView(generic.CreateView):
    model = Club
    form_class = ClubForm


class ClubUpdateView(generic.UpdateView):
    model = Club
    form_class = ClubForm


class ClubDetailView(generic.DetailView):
    model = Club


class ClubDeleteView(generic.DeleteView):
    model = Club
    success_url = reverse_lazy("football:club-list")
    template_name = "football/club_confirm_delete.html"


class CoachListView(generic.ListView):
    model = Coach
    template_name = "football/coach_list.html"
    context_object_name = "coaches_list"


class CoachCreateView(generic.CreateView):
    model = Coach
    form_class = CoachForm


class CoachUpdateView(generic.UpdateView):
    model = Coach
    form_class = CoachForm


class CoachDetailView(generic.DetailView):
    model = Coach


class CoachDeleteView(generic.DeleteView):
    model = Coach
    success_url = reverse_lazy("football:coach-list")
    template_name = "football/coach_list.html"
