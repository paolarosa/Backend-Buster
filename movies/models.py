from django.db import models
from users.models import User

class RatingMovie(models.TextChoices):
    G = "G",
    PG = "PG",
    PG_13 = "PG-13",
    R = "R",
    NC_17 = "NC-17"

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(max_length=20, choices = RatingMovie.choices, default= RatingMovie.G)
    synopsis = models.TextField(null=True, default=None)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="movie", null=True)
    orders = models.ManyToManyField("users.User", through="MovieOrder", related_name="movies")
 
    def __str__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"

class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user_movie")
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="order_movie")