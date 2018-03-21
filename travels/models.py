from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


# Create your models here.


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', default='profile_images/default.png', blank=True)

    def __str__(self):
        return self.user.username


# author, author_id, comment, content, id, picture, publish_date, slug, tags, title
class Article(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE )
    title = models.CharField(max_length=128)
    tags = models.CharField(max_length=128)
    content = models.TextField()
    picture = models.FileField(upload_to='article_images', blank=True)
    publish_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.article.title
