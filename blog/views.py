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


def post(request, id):
    print('post', id)

    context = {
        # 'text': 'Página do Blog',
        'title': 'POST - ',
        'posts': posts
    }
    return render(
        request,
        'blog/index.html',
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
