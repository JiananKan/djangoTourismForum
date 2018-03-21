from django import forms
from travels.models import UserProfile, Article, Comment
from django.contrib.auth.models import User
from django.forms.widgets import FileInput

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class ArticleForm(forms.ModelForm):
    # picture = forms.FileField(widget=FileInput)
    class Meta:
        model = Article
        fields = ('title', 'tags', 'content', 'picture',)



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
