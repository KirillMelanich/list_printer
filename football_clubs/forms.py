from django import forms

from football_clubs.models import Club, Coach


class ClubForm(forms.ModelForm):

    class Meta:
        model = Club
        fields = "__all__"


class CoachForm(forms.ModelForm):

    class Meta:
        model = Coach
        fields = "__all__"