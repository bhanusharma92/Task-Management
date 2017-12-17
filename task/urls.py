from django.conf.urls import url

from . import views

app_name = 'task'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^after_login', views.after_login, name='after_login'),
    url(r'^sign_up', views.sign_up, name='sign_up'),
    url(r'^sign_in', views.sign_in, name='sign_in'),
    url(r'^sign_out', views.sign_out, name='sign_out'),
    url(r'^add_task', views.add_task, name='add_task'),
    url(r'^view_task', views.view_task, name='view_task'),
    url(r'^delete_task', views.delete_task, name='delete_task'),
]

