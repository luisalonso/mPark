from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^guide/$', views.guide, name='guide'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^professional/profile/(?P<pk>[0-9]+)/(?P<pp>[0-9]+)/$', views.profile_detail, name='profile_detail'),
    url(r'^professional/profile/(?P<pk>[0-9]+)/(?P<pp>[0-9]+)/(?P<t1>[0-9]+)/$', views.session_update, name='profile_detail'),
    url(r'^session/save/(?P<pk>[0-9]+)/(?P<pp>[0-9]+)/(?P<t1>[0-9]+)/$', views.session_update, name='profile_detail'),
    url(r'^session/save/$', views.session_update, name='session_save'),

    url(r'^professional/explore_data/$', views.explore_data, name='explore_data'),
    url(r'^professional/explore_data/raw_data/$', views.raw_data, name='raw_data'),

    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]
