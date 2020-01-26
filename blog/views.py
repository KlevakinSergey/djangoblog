from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.base import View
from blog.models import Post, Tag
from .utils import ObjectDetailMixin
from .forms import TagForm, PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})

class PostDetail(ObjectDetailMixin, View):
    # model = Post
    # template = 'blog/post_detail.html'
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact= slug )
        return render(request, 'blog/post_detail.html', {'post': post}) 

class TagDetail(ObjectDetailMixin, View):
    # model = Tag
    # template = 'blog/tag_detail.html'
    def get(self, request, slug):
        tag = get_object_or_404(Tag ,slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', {'tag': tag})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', {'form':form} )

    def post(self, request):
        bound_form = PostForm(request.POST, request.FILES)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return  render(request, 'blog/post_create.html', {'form':bound_form})   
    


class TagCreate(View):
    def get(self, request):
        form = TagForm()   
        return render(request, 'blog/tag_create.html', {'form':form})     

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return  render(request, 'blog/tag_create.html', {'form':bound_form})   


    


     

