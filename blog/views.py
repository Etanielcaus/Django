# from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts
from typing import Any


def blog(request):

    context = {
        'text': 'Página do Blog',
        'title': 'Estamos no Blog - ',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
        context
    )


def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não encontrado')

    context = {
        # 'text': 'Página do Blog',
        'title': found_post['title'] + ' - ',
        # 'posts': posts
        'post': found_post
    }

    return render(
        request,
        'blog/post.html',
        context
    )


def exemplo(request):
    context = {
        'text': 'Estamos no Exemplo',
        'title': 'Essa é uma pagina de exemplo - '
    }
    return render(
        request,
        'blog/exemplo.html',
        context
    )
