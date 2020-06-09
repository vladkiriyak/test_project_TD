from rest_framework import serializers

from .models import Post, Comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        comment = Comment.objects.update_or_create(
            id=validated_data.get('id'),
            defaults={
                'text': validated_data.get('text'),
                'username': validated_data.get('username'),
                'post': validated_data.get('post')
            }

        )
        return comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        post = Post.objects.update_or_create(
            uuid=validated_data['uuid'],
            defaults={
                'title': validated_data.get('title'),
                'text': validated_data.get('text'),
                'votes': validated_data.get('votes'),
                'username': validated_data.get('username'),
            }

        )
        return post


class PostSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('uuid', 'title', 'votes')
