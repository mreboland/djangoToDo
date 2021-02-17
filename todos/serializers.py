# We need a serializer to transform our data from the models into JSON that will be outputted at the URLs.
# Importing serializers from django rest framework
from rest_framework import serializers
# importing our Todo model
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = (
            # id is created automatically by django so we didn't have to define it in our Todo model
            "id",
            "title",
            "body",
        )