from django.shortcuts import render


def root(request):

    data = {
        'title': 'Главная страница',
        'values': ['some', 'nigga', 'body', 'was', 'a', 'told', 'me', 123],
        'fantasy': {
            'car': 'mustang',
            'age': 21,
        }
    }
    return render(request, 'main/main.html', data)


def matrix_rain(request):
    return render(request, 'main/matrix_rain.html')


def about(request):
    return render(request, 'main/about.html')