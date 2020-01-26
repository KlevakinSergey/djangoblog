from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.base import View
from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm
from django.urls import reverse


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})

class PostDetail(View):
    # model = Post
    # template = 'blog/post_detail.html'
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact= slug )
        return render(request, 'blog/post_detail.html', {'post': post}) 

class TagDetail(View):
    # model = Tag
    # template = 'blog/tag_detail.html'
    def get(self, request, slug):
        tag = get_object_or_404(Tag ,slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', {'tag': tag})



class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'




class PostCreate(ObjectCreateMixin,View):
    model_form = PostForm
    template = 'blog/post_create.html'

 


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'post_list_url'


    


class TagCreate(ObjectCreateMixin, View):

    model_form = TagForm
    template = 'blog/tag_create.html'

     
        

class TagUptate(ObjectUpdateMixin ,View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'
   



class TagDelete(ObjectDeleteMixin ,View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'





     

