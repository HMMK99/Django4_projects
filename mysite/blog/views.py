from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView
# from django.core.paginator import Paginator, EmptyPage,\
                                #   PageNotAnInteger

# Create your views here.

class PostListView(ListView):
    queryset = Post. published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    return render(request,
                  'blog/post/detail.html',
                  {'post':post, })
