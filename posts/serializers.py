from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    class Meta: # take these fields from Post model for transforms data into JSON
        fields = ('id','author','title','body','created_at',)
        model = Post
