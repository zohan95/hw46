from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Article, status_choices
from .forms import PostForm
from django.views.generic import View


def todo_view(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'index.html', {'articles': articles, 'choices': status_choices})
    elif request.method == 'POST':
        articles = request.POST.getlist('item')
        str_todo = '-'.join(articles)
        return render(request, 'deletepocket.html', {'articles': str_todo})


class todo_create(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'todo_create_form.html', context={'form': form})

    def post(self, request):
        bound_from = PostForm(request.POST)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'todo_create_form.html', context={'form': bound_from})


def detail_view(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'detail.html', {'article': article, 'choices': status_choices})


class edit_view(View):
    def get(self, request, pk):
        article = Article.objects.get(pk=pk)
        form = PostForm(instance=article)
        return render(request, 'todo_edit_form.html', context={'form': form, 'pk1': article.pk})

    def post(self, request, pk):
        obj = Article.objects.get(pk=pk)
        bound_from = PostForm(request.POST, instance=obj)
        if bound_from.is_valid():
            bound_from.save()
            return redirect('main_url')
        return render(request, 'todo_edit_form.html', context={'form': bound_from})


def todo_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('main_url')


def todos_delete(request, articles):
    if request.method == 'POST':
        mass_todo = articles.split('-')
        for i in mass_todo:
            article = Article.objects.get(pk=int(i))
            article.delete()
        return redirect('main_url')
