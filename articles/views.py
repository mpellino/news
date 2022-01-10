from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Article
from django.urls import reverse_lazy
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')


class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = "article_edit.html"


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'author')
    template_name = "article_new.html"
