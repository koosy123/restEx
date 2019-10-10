from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post # Post를 기반으로 직렬화 시킬 것.
        fields = ['title','body']