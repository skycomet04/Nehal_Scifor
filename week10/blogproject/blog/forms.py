from django import forms
from blog.models import Blog,Contact,Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content','image']
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'desc','email']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment_desc']