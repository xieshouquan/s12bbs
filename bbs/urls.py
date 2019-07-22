
from django.conf.urls import url,include
from django.urls import re_path

from bbs import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^category/(\d+)/$',views.category,name='category_detail'),
    re_path(r'^detail/(\d+)/$',views.ariticle_detail,name='article_detail'),
    re_path(r'^comment/$',views.comment,name='post_comment'),
    re_path(r'^comment_list/(\d+)/$',views.get_comments,name='get_comments'),
    re_path(r'^new_article/$',views.new_article,name='new-article'),
    re_path(r'^file_upload/$',views.file_upload,name='file-upload'),
    re_path(r'^latest_article_count/$',views.get_latest_article_count,name='get_latest_article_count'),
]
