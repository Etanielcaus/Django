# from django.http import HttpResponse

from django.shortcuts import render
from blog.data import posts


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


def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    context = {
        # 'text': 'Página do Blog',
        'title': 'POST - ',
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
