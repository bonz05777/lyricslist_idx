from django.shortcuts import render, get_object_or_404
from .models import Post 
from django.http import HttpResponseRedirect
from .forms import PostForm
from rest_framework import generics
from .serializers import PostSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


def blog_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)

    if request.method == 'POST':
        print("Form data:", request.POST)  # Check submitted form data
        if form.is_valid():
            print("Form is valid. Saving...")
            form.save()
            return HttpResponseRedirect('/posts/')  # Redirect after saving
        else:
            print("Form errors:", form.errors)  # Check form errors

    context = {
        "form": form,
        "form_type": "Update"
    }
    return render(request, "blog/blog_create.html", context)

def blog_create(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()  # Save the form
        return HttpResponseRedirect('/posts/')  # Redirect to the post list

    context = {
        "form": form,
        "form_type": "Create"
    }
    return render(request, "blog/blog_create.html", context)

def blog_list(request):
    posts = Post.objects.all()
    context = {
        "blog_list": posts
    }
    return render(request, "blog/blog_list.html", context)

def blog_detail(request, id):
    each_post = get_object_or_404(Post, id=id)
    context = {
        "blog_detail": each_post
    }
    return render(request, "blog/blog_detail.html", context)

def blog_delete(request, id):
    each_post = get_object_or_404(Post, id=id)
    each_post.delete()
    return HttpResponseRedirect('/posts/')
