from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Articles
from .forms import ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete_post_page.html'
    success_url = '/news/'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create_post_page.html'
    form_class = ArticlesForm


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/news_detail.html'
    context_object_name = 'article'


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



