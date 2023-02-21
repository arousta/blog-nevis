from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post

        fields = [
            "pk",
            "author",
            "title",
            "text",
            "comments",
        ]

        read_only_fields = [
            "pk",
            "author",
        ]
