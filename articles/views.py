from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Article


class ArticleListView ( ListView ) :
    model = Article
    template_name = 'home.html'
    context_object_name = 'articles'
    ordering = ['-id']


class ArticleDetailView ( DetailView ) :
    model = Article
    template_name = 'Article/article_detail.html'
    context_object_name = 'article'


class ArticleCreateView ( LoginRequiredMixin, CreateView ) :
    model = Article
    template_name = 'Article/article_new.html'
    fields = ['title', 'summary', 'body', 'photo']

    def form_valid(self, form) :
        form.instance.author = self.request.user
        return super ().form_valid ( form )


class ArticleUpdateView ( LoginRequiredMixin, UserPassesTestMixin, UpdateView ) :
    model = Article
    template_name = 'Article/article_edit.html'
    fields = ['title', 'summary', 'body', 'photo']

    def test_func(self) :
        article = self.get_object ()
        return self.request.user == article.author


class ArticleDeleteView ( LoginRequiredMixin, UserPassesTestMixin, DeleteView ) :
    model = Article
    template_name = 'Article/article_delete.html'
    success_url = reverse_lazy ( 'home' )

    def test_func(self) :
        article = self.get_object ()
        return self.request.user == article.author