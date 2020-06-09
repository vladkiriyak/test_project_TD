from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostListView.as_view()),
    path("post/", views.PostView.as_view()),
    path("post/<uuid>/<method>", views.PostView.as_view()),
    path("post/<uuid>/", views.PostView.as_view()),
    path("comment/", views.CommentView.as_view()),
]
