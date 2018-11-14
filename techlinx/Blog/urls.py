from django.conf.urls import url
from django.contrib import admin
from .views import index,post,Categories#add_comment_to_post


urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^posts/(?P<slug>[\w-]+)/$', post,name="post"),
    #url(r'^post/(?P<pk>\d+)/comment/$', add_comment_to_post, name='add_comment_to_post'),
]
