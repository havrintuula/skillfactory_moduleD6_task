from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.
class NewsList(ListView):
    model = Post
    ordering = '-posted'
    # queryset = Product.objects.filter(price__lt=1000000).order_by('-name')
    template_name = 'news_list.html'
    context_object_name = 'news_list'


class NewsId(DetailView):
    model = Post
    template_name = 'news_id.html'
    context_object_name = 'news_id'

