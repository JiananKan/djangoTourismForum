from django.conf.urls import url
from travels import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'base/$', views.base, name='base'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^add_article/$', views.add_article, name='add_article'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^my_article/$', views.my_article, name='my_article'),
    url(r'^delete/(\d+)/$', views.delete_article, name='delete_article'),
    url(r'^edit/(\d+)/$', views.edit, name='edit_article'),
    url(r'^article/(\d+)/$', views.show_article, name='show_article'),
    url(r'^comment/(\d+)/$', views.comment, name='comment'),
    url(r'^content', views.content)




]
