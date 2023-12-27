from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from football_clubs.forms import ClubForm
from football_clubs.models import Club


def index(request):
    """View function for the home page of the site."""

    num_clubs = Club.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_clubs": num_clubs,
        "num_visits": num_visits + 1,
    }

    return render(request, "index.html", context=context)


class ClubsListView(generic.ListView):
    model = Club
    template_name = "football_clubs/club_list.html"
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
    success_url = reverse_lazy("football_clubs:club-list")
    template_name = "football_clubs/club_confirm_delete.html"
