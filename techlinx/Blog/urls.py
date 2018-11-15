from django.conf.urls import url
from django.contrib import admin
from .views import index,post,categories#add_comment_to_post


urlpatterns = [
    url(r'^$', index,name="index"),
    url(r'^posts/(?P<slug>[\w-]+)/$', post,name="post"),
    url(r'^categorias/(?P<slug>[\w-]+)/$', categories, name="categorias")
]
