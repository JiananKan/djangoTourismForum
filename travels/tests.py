from django.test import TestCase
from django.test import Client
# Create your tests here.
from travels.models import Article, UserProfile, User, Comment


class UserTests(TestCase):
    def test_login(self):
        print('test login')
        user = User.objects.create(username="Ason", email="jj@gmail.com")
        user.set_password('123456')
        user.save()
        c = Client()
        logged_in = c.login(username='Ason', password='123456')
        print('test login success!')
        return logged_in


class ArticleTests(TestCase):
    def test_addarticle(self):
        print('test add article')
        user = User.objects.create(username="Ason", email="jj@gmail.com")
        user.set_password('123456')
        user.save()
        userprofile = UserProfile.objects.create(user_id=1)
        userprofile.user = user

        user = User.objects.get(username='Ason')
        userprofile = UserProfile.objects.get(user=user)
        title = "England!!Glasgow!"
        article = Article.objects.create(author=user, title=title)
        article.tags = "England Travel"
        article.content = "I like to traveling! I like England!"
        saved = article.save()
        print('test add article success!')
        return saved


class CommentTests(TestCase):
    def test_addcomment(TestCase):
        print('test add comment')
        user = User.objects.create(username="Ason", email="jj@gmail.com")
        user.set_password('123456')
        user.save()
        userprofile = UserProfile.objects.create(user_id=1)
        userprofile.user = user

        user = User.objects.get(username='Ason')
        userprofile = UserProfile.objects.get(user=user)
        title = "England!!Glasgow!"
        article = Article.objects.create(author=user, title=title)
        article.tags = "England Travel"
        article.content = "I like to traveling! I like England!"
        saved = article.save()

        user = User.objects.get(username='Ason')
        article = Article.objects.get(author=user)
        comment = 'test comment!'
        comment_creat = Comment.objects.create(article=article, user=user, comment=comment)

        print('test add article success!')
        return saved
