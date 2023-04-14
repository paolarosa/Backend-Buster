from rest_framework import serializers
from .models import RatingMovie, Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(choices = RatingMovie.choices, allow_null=True, default= RatingMovie.G)
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def get_added_by(self, obj):
        user = obj.user.email
        return user

    def create(self, validated_data:dict):
        return Movie.objects.create(**validated_data)

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField()
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)

    def get_title(self, obj):
        title = obj.movie.title
        return title
    
    def get_buyed_by(self, obj):
        buyed_by = obj.user.email
        return buyed_by