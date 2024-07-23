from django.shortcuts import render
from blog.models import Posts, Category
from django.db.models import Q

def main_page(request):
    posts = Posts.objects.all()
    categories = Category.objects.all()
    text  = request.GET.get("search",None)
    category = request.GET.get("cat",None)
    if text:
        posts = posts.filter(Q(title__icontains =  text)|Q(body__icontains = text))
    if category:
        posts = posts.filter(category_id = category)
    context = {
        "posts":posts,
        "categories":categories
    }
    return render(request, "main.html", context)


def post_details(request, post_id):
    try:
        post = Posts.objects.get(id=post_id)

    except Posts.DoesNotExist:
        post = None

    context = {
        'post': post
    }
    return render(request, "detail.html", context)
# Create your views here.
