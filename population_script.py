import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoforum.settings')
import django

django.setup()
from travels.models import UserProfile, Article, Comment, User


def populate():
    python_user = [
        {"username": "jason",
         "password": "123456",
         "email": "xman@gmail.com",
         "user_id": "2"},
        {"username": "vanke",
         "password": "123456",
         "email": "xwoman@gmail.com",
         "user_id": "3"}
    ]

    python_article = [
        {"title": "Caffeine cultures fisrt",
         "tags": "Caffeine first",
         "content": "Despite their reputation as tea aficionados, Britain is fast becoming a nation of coffee drinkers, "
                    "consuming around 55 million cups a day. Coffee does more than battle a hangover and keep us alert – "
                    "it has also been linked to productivity in the workplace. Then there are the social"
                    " benefits: who doesn’t love a good old natter over a hot cup of coffee?"},

        {"title": "Caffeine cultures second",
         "tags": "Caffeine second",
         "content": "Despite their reputation as tea aficionados, Britain is fast becoming a nation of coffee drinkers, "
                    "consuming around 55 million cups a day. Coffee does more than battle a hangover and keep us alert – "
                    "it has also been linked to productivity in the workplace. Then there are the social"
                    " benefits: who doesn’t love a good old natter over a hot cup of coffee?"},

        {"title": "Caffeine cultures third",
         "tags": "Caffeine third",
         "content": "Despite their reputation as tea aficionados, Britain is fast becoming a nation of coffee drinkers, "
                    "consuming around 55 million cups a day. Coffee does more than battle a hangover and keep us alert – "
                    "it has also been linked to productivity in the workplace. Then there are the social"
                    " benefits: who doesn’t love a good old natter over a hot cup of coffee?"},

        {"title": "Caffeine cultures forth",
         "tags": "Caffeine fourth",
         "content": "Despite their reputation as tea aficionados, Britain is fast becoming a nation of coffee drinkers, "
                    "consuming around 55 million cups a day. Coffee does more than battle a hangover and keep us alert – "
                    "it has also been linked to productivity in the workplace. Then there are the social"
                    " benefits: who doesn’t love a good old natter over a hot cup of coffee?"},

    ]

    python_comment = [
        {"comment": "Very great experience!"},
        {"comment": "Id love to know how much this costed, looks amazing. If you dont mind what was your budget?"},
        {"comment": "I would love to know how much this trip costed?"}
    ]

    # for user in python_user:
    #     user_add = add_user(user['username'], user["password"],
    #                         user["email"], user["user_id"])

    # for article in python_article:
    #     article_add = add_article(article['title'], article['tags'],
    #                               article['content'])

    for comment in python_comment:
        comment_add = add_comment(comment['comment'])


def add_user(name, password, email, userid):
    userprofile = UserProfile.objects.create(user_id=userid)
    user = User.objects.create()
    user.username = name
    user.set_password(password)
    user.email = email
    user.save()
    userprofile.user = user
    userprofile.save()
    return userprofile


def add_article(title, tags, content):
    user = User.objects.get(username='jason')
    userprofile = UserProfile.objects.get(user=user)
    article = Article.objects.create(author=user, title=title)
    article.tags = tags
    article.content = content
    article.save()

    # print(title)
    return userprofile


def add_comment(comment):
    articles = Article.objects.all()
    for art in articles:
        user = User.objects.get(username='jason')
        comment_creat = Comment.objects.create(article=art, user=user, comment=comment)
        user = User.objects.get(username='vanke')
        comment_creat = Comment.objects.create(article=art, user=user, comment=comment)

    return articles


if __name__ == '__main__':
    print("Starting Travels population script...")
    populate()
