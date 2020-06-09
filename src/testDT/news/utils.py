import uuid

from news.models import Post
from testDT.settings import BASE_URL


def get_uuid() -> str:
    return uuid.uuid4().hex


def insert_urls(data: dict) -> dict:
    for d in data:
        d["url"] = BASE_URL + "news/post/" + d["uuid"]

    return data


def get_post_id(uuid: str) -> int:
    post = Post.objects.get(uuid=uuid)
    return post.id
