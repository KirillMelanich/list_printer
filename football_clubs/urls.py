from django.urls import path

from football_clubs.views import (
    index,
    ClubListView,
    ClubCreateView,
    ClubUpdateView,
    ClubDeleteView,
    ClubDetailView,
    CoachListView,
    CoachCreateView,
    CoachUpdateView,
    CoachDeleteView,
    CoachDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path("home/", index, name="index"),
    path("clubs/", ClubListView.as_view(), name="club-list"),
    path("clubs/create/", ClubCreateView.as_view(), name="club-create"),
    path("clubs/<int:pk>/update/", ClubUpdateView.as_view(), name="club-update"),
    path("clubs/<int:pk>/delete/", ClubDeleteView.as_view(), name="club-delete"),
    path("clubs/<int:pk>/detail/", ClubDetailView.as_view(), name="club-detail"),
    path("coaches/", CoachListView.as_view(), name="coach-list"),
    path("coaches/create/", CoachCreateView.as_view(), name="coach-create"),
    path("coaches/<int:pk>/update/", CoachUpdateView.as_view(), name="coach-update"),
    path("coaches/<int:pk>/delete/", CoachDeleteView.as_view(), name="coach-delete"),
    path("coaches/<int:pk>/detail/", CoachDetailView.as_view(), name="coach-detail"),
]

app_name = "football_clubs"
