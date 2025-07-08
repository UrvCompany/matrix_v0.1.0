from django.shortcuts import render
from .models import Articles


def news_home(request):
    news = Articles.objects.all()

    # news = Articles.objects.order_by('-date')[:1]      Доп фишки

    return render(request, 'news/news_home.html', {'news': news})
