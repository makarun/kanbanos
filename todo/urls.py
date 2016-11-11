from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'todo/$', views.task_todo_list, name='task_todo_list'),
    url(r'doing/$', views.task_doing_list, name='task_doing_list'),
    url(r'done/$', views.task_done_list, name='task_done_list'),
    url(r'aborted/$', views.task_aborted_list, name='task_aborted_list'),
    url(r'add/$', views.task_add, name='task_add'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.task_detail, name='task_detail'),
    url(r'^task/(?P<pk>[0-9]+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^task/(?P<pk>\d+)/remove/$', views.task_remove, name='task_remove'),
    url(r'^task/(?P<pk>\d+)/stage/$', views.add_stage_to_task, name='add_stage_to_task'),
    url(r'^stage/(?P<pk>\d+)/remove/$', views.stage_remove, name='stage_remove'),
    url(r'^stage/(?P<pk>\d+)/change_achieved/$', views.change_achieved, name='change_achieved'),


]


