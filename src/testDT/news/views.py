from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment
from .serializers import PostListSerializer, PostSerializer, CommentCreateSerializer, PostCreateSerializer
from .utils import get_uuid, insert_urls, get_post_id


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostListSerializer(posts, many=True)
        data = serializer.data
        insert_urls(data)
        return Response(data=data)


class PostView(APIView):

    def get(self, request, uuid):
        post = Post.objects.get(uuid=uuid)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, uuid, method):

        if method == 'upvote':
            post = Post.objects.get(uuid=uuid)
            post.votes += 1

            post.save()
            return Response(status=204)
        else:
            data = request.data
            post_serializer = PostCreateSerializer(data=data)
            if post_serializer.is_valid():
                post_serializer.save()
                return Response(status=204)

    def post(self, request):
        data = request.data
        data['uuid'] = get_uuid()
        post = PostCreateSerializer(data=data)
        if post.is_valid():
            post.save()
            return Response(status=201)

    def delete(self, request, uuid):
        post = Post.objects.get(uuid=uuid)
        if post:
            post.delete()
            return Response(status=204)
        else:
            return Response(status=404)


class CommentView(APIView):

    def delete(self, request):
        comment = Comment.objects.get(uuid=request.data['id'])
        if comment:
            comment.delete()
            return Response(status=204)
        else:
            return Response(status=404)

    def put(self, request):
        data = request.data
        comment_serializer = CommentCreateSerializer(data=data)
        if comment_serializer.is_valid():
            comment_serializer.save(id=data['id'])
            return Response(status=204)

    def post(self, request):
        data = request.data
        data['post'] = get_post_id(uuid=request.data['post'])
        comment = CommentCreateSerializer(data=data)
        if comment.is_valid():
            comment.save()
            return Response(status=201)
