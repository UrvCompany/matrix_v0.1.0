from django.shortcuts import render


def root(request):
    return render(request, 'main/main.html')


def matrix_rain(request):
    return render(request, 'main/matrix_rain.html')


def about(request):
    return render(request, 'main/about.html')