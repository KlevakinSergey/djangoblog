from django import forms
from blog.models import Tag, Post, Comment
from django.core.exceptions import ValidationError





class TagForm(forms.ModelForm):
   

    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-conrol'}),
            'slug': forms.TextInput(attrs={'class':'form-conrol'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be CREATE')

        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Slug must be unique. We have {new_slug} slug already')
        return new_slug


class PostForm(forms.ModelForm):
    class Meta:

        model = Post
        fields = ['title', 'slug', 'body', 'image',  'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-conrol'}),
            'slug': forms.TextInput(attrs={'class':'form-conrol'}),
            'body': forms.Textarea(attrs={'class':'form-conrol'}),
            'image': forms.FileInput(),
            'tags': forms.SelectMultiple(attrs={'class':'form-conrol'}),
            
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be CREATE')
        return new_slug    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
