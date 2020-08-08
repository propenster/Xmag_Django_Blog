from django.shortcuts import get_object_or_404, render
from .models import Category
from .models import Article

# Create your views here.
def category_list(request):
    category_list = Category.objects.all()
    return render(request, 'blog/index.html', {'category_list':category_list})

def index(request):
    article_thumb = Article.objects.order_by('-published', 'category')[:2]
    article_list = Article.objects.order_by('-published')[:3]

    return render(request, 'blog/index.html', {'article_thumb':article_thumb, 'article_list':article_list})
# def home(request):
#     post_list = Article.objects.all()
#     return render(request, 'blog/home', {'post_list':post_list})


def article_detail(request, post_id):
    post = get_object_or_404(Article, pk=post_id)
    return render(request, 'blog/detail', {'post':post})