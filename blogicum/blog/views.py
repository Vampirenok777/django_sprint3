from django.shortcuts import render, get_object_or_404
from .models import Location, Category, Post
import datetime


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.filter(is_published=True,
                                    category_id__is_published=True,
                                    pub_date__lt=datetime.datetime.now()
                                    ).order_by('created_at')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(Post,
                             pk=id,
                             is_published=True,
                             category__is_published=True,
                             pub_date__lt=datetime.datetime.now()
                             )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True
                                 )
    post_list = Post.objects.filter(is_published=True,
                                    category_id=category.pk,
                                    pub_date__lt=datetime.datetime.now()
                                    )
    context = {'post_list': post_list}
    return render(request, template, context)
