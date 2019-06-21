from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .forms import ArticleForm
from .models import Article


def index(request):
    return render(request, 'stock/base.html')


class ArticleListView(ListView):
    """
    View for listing articles
    """
    model = Article
    template_name = 'stock/article_list.html'


class ArticleDetailView(DetailView):
    """
    Detail view for a Article
    """
    model = Article
    template_name = 'stock/article_detail.html'


class ArticleCreateView(CreateView):
    """
    View for creating a Article
    """
    model = Article
    form_class = ArticleForm
    template_name = 'stock/article_form.html'
    success_url = reverse_lazy('stock:article_list')


class ArticleUpdateView(UpdateView):
    """
    View for updating a Article
    """
    model = Article
    form_class = ArticleForm
    template_name = 'stock/article_form.html'
    success_url = reverse_lazy('stock:article_list')


class ArticleDeleteView(SuccessMessageMixin, DeleteView):
    """
    View for deleting a article
    """
    model = Article
    template_name = 'stock/article_delete.html'
    success_url = reverse_lazy('stock:article_list')
    success_message = ugettext_lazy('The operation was successful.')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ArticleDeleteView, self).delete(request, *args, **kwargs)
