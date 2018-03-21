from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
# from django.urls import reverse
from json import *
from travels.forms import UserForm, UserProfileForm, ArticleForm, CommentForm
from travels.models import Article, UserProfile, Comment


# Create your views here.


def index(request):
    articles = Article.objects.all()

    context_dit = {'articles': articles}
    return render(request, 'travels/index.html', context_dit)


def base(request):
    context_dit = {}
    article = Article.objects.all()
    context_dit['article'] = article

    return render(request, 'travels/base.html', context_dit)


@login_required
def user_profile(request):
    context_dit = {}
    user_obj = UserProfile.objects.get(user=request.user)
    context_dit['userprofle'] = user_obj

    return render(request, 'travels/profile.html', context_dit)


@login_required
def my_article(request):
    context_dit = {}
    articles = Article.objects.filter(author=request.user)

    context_dit['articles'] = articles
    # print("user article:" + articles.title)

    return render(request, 'travels/my_article.html', context_dit)


def edit(request, article_id):
    form = ArticleForm()
    article_old = Article.objects.get(pk=article_id)
    form.fields["title"].initial = article_old.title
    form.fields["tags"].initial = article_old.tags
    form.fields["content"].initial = article_old.content
    form.fields["picture"].initial = article_old.picture
    context_dict = {}

    # A HTTP Method
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article_old.title = article.title
            article_old.tags = article.tags
            article_old.content = article.content
            article_old.picture = request.FILES.get('picture')
            article_old.save()
            return HttpResponseRedirect(reverse('my_article'))
        else:
            print(form.errors)

    context_dict['form'] = form
    context_dict['article'] = article_old
    return render(request, 'travels/edit_article.html', context_dict)


def delete_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    article.delete()

    return HttpResponseRedirect(reverse('my_article'))


def register(request):
    registered = False

    # if it is a HTTP POST, we are interested in processing data
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # save user's form data to dbase
            user = user_form.save()
            # hash password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            # Get picture if provided
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            # Save the UserProfile model instance
            profile.save()
            # Registration successful
            registered = True
        else:
            # Invalid forms
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'travels/register.html', {'user_form': user_form,
                                                     'profile_form': profile_form,
                                                     'registered': registered})


def user_login(request):
    # pull out relevant information if it's HTTP POST
    if request.method == 'POST':
        # Gather username and password provided by the user.
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if valid
        user = authenticate(username=username, password=password)
        # If we have a user object, the details are correct
        if user:
            if user.is_active:
                # send user back to homepage
                login(request, user)
                return HttpResponseRedirect(reverse('index'))  #
            else:
                # an inactive account
                return HttpResponse("Your Rango account is disabled.")
        else:
            # bad login details provided
            print("Invalid login details:{0}, {1}".
                  format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # Request is not HTTP POST
    else:
        # no context variable to pass to the template system
        return render(request, 'travels/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    # Back to homepage
    return HttpResponseRedirect(reverse('index'))  # # HttpResponse(reverse('index'))


@csrf_exempt
def add_article(request):
    form = ArticleForm()
    context_dict = {}
    # A HTTP Method
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.picture = request.FILES.get('picture')

            article.save()
            return HttpResponseRedirect("/travels/")
        else:
            print(form.errors)

    context_dict['form'] = form
    return render(request, 'travels/add_article.html', context_dict)


@login_required
def show_article(request, article_id):
    context_dict = {}
    form = CommentForm()
    article = Article.objects.get(pk=article_id)
    user_obj = UserProfile.objects.get(user=request.user)
    context_dict['userprofle'] = user_obj
    context_dict['article'] = article
    context_dict['comment_counts'] = Comment.objects.filter(article=article).count()
    context_dict['comments'] = Comment.objects.filter(article=article)
    context_dict['form'] = form
    return render(request, 'travels/article_page.html', context_dict)


def comment(request, article_id):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_id)
        direct_path = "/travels/article/" + str(article_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.article = article
            comment.save()

            return HttpResponseRedirect(direct_path)
        else:
            print(form.errors)

    # return render(request, request.path_info, {})
    return render(request, direct_path, {})


@csrf_exempt
def content(request):
    if request.method == 'POST':
        text = request.POST.get('HHS', 'null')
        a = {'pm': text}
        return HttpResponse(dumps(a), content_type='application/json')
