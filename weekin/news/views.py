from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'news/post/post_list.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug = post,
                             status = 'published',
                             week_end__year = year,
                             week_end__month = month,
                             week_end__day = day)

    return render(request, 'news/post/detail.html', {'post':post})

