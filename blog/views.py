from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.base import View
from .models import Post, Tag, Comment
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import TagForm, PostForm, CommentForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

def post_list(request):
    search_query = request.GET.get('search', '')
    
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
    else:
        posts = Post.objects.all()

            
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    
    is_paginated = page.has_other_pages()
    
    if page.has_previous():
        prev_url= f'?page={page.previous_page_number()}'

    else:
        prev_url = ''    

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'

    else:
        next_url = ''

    context = {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    return render(request, 'blog/index.html', context=context)
    


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', {'tags': tags})

class PostDetail(View):
    # model = Post
    # template = 'blog/post_detail.html'
    def get(self, request, slug):
        post = get_object_or_404(Post, slug__iexact= slug )
        comments = post.comments.filter(active=True)
        comment_form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form}) 
    
    def post(self, request, slug):
        comment_form = CommentForm(data=request.POST)
        post = get_object_or_404(Post, slug__iexact= slug )
        comments = post.comments.filter(active=True)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
        return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form}) 

class TagDetail(View):
    # model = Tag
    # template = 'blog/tag_detail.html'
    def get(self, request, slug):
        tag = get_object_or_404(Tag ,slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', {'tag': tag})



class PostUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'blog/post_update.html'
    raise_exception =True




class PostCreate(LoginRequiredMixin, ObjectCreateMixin,View):
    model_form = PostForm
    template = 'blog/post_create.html'
    raise_exception =True

 


class PostDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'post_list_url'
    raise_exception =True


    


class TagCreate(LoginRequiredMixin, ObjectCreateMixin, View):

    model_form = TagForm
    template = 'blog/tag_create.html'
    raise_exception =True

     
        

class TagUptate(LoginRequiredMixin, ObjectUpdateMixin ,View):
    model = Tag
    model_form = TagForm
    template = 'blog/tag_update.html'
    raise_exception =True
   



class TagDelete(LoginRequiredMixin, ObjectDeleteMixin ,View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'
    raise_exception =True







     

