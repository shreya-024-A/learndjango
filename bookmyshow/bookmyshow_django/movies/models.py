from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Movie(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    duration = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    poster = models.ImageField(upload_to='posters/',
                               null=True,
                               blank=True)

# Create your models here.
    def __str__(self):
        return self.title