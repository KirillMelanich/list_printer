from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

from django.urls import reverse


class Coach(models.Model):
    first_name = models.CharField(max_length=255, unique=False, blank=False, null=False)
    last_name = models.CharField(max_length=255, unique=False, blank=False, null=False)
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(18, message="Coach can't be younger than 18"),
            MaxValueValidator(90, message="Coach can't be older than 90"),
        ],
    )
    nationality = models.CharField(
        max_length=255, unique=False, blank=False, null=False
    )

    class Meta:
        verbose_name_plural = "coaches"

    def get_absolute_url(self):
        return reverse("football:coach-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Club(models.Model):
    coach = models.OneToOneField(
        Coach, related_name="club", on_delete=models.SET_NULL, null=True
    )
    name = models.CharField(max_length=255, unique=False, blank=False, null=False)
    city = models.CharField(max_length=255, unique=False, blank=False, null=False)
    country = models.CharField(max_length=255, unique=False, blank=False, null=False)
    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1700, message="Year must be 1700 or greater."),
            MaxValueValidator(
                datetime.datetime.now().year, message="Year cannot be in the future."
            ),
        ],
    )

    class Meta:
        unique_together = ["name", "city"]

    def get_absolute_url(self):
        return reverse("football:club-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.name}  {self.city} - {self.year}"
