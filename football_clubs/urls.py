from django.urls import path

from football_clubs.views import index, ClubsListView, ClubCreateView, ClubUpdateView, ClubDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="index"),
    path("clubs/", ClubsListView.as_view(), name="club-list"),
    path("clubs/create/", ClubCreateView.as_view(), name="club-create"),
    path("clubs/<int:pk>/update/", ClubUpdateView.as_view(), name="club-update"),
    path("clubs/<int:pk>/delete/", ClubDeleteView.as_view(), name="club-delete"),
]

app_name = "football_clubs"
