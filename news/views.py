from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.all()

    # news = Articles.objects.order_by('-date')[:1]      Доп фишки

    return render(request, 'news/news_home.html', {'news': news})


def create_post(request):

    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Ты что творишь, шелуха?'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'news/create_post_page.html', data)



