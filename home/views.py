from django.shortcuts import render


def home(request):
    print('home')

    context = {
        # 'text': 'Estamos na Home'
    }

    return render(
        request,
        'home/index.html',
        context,
    )
