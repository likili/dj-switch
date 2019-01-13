from django.conf.urls import url
from django.urls import path
from blocks import views

app_name = 'blocks'
urlpatterns = [
    url(r'^$', views.TitleView.as_view(), name='list'),
    # url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
    # url(r'add/$', views.StudentCreateView.as_view(), name='add'),
    # url(r'edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
    # url(r'remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
]


# urlpatterns = [
#     url(r'^$', views.StudentListView.as_view(), name='list'),
#     url(r'^(?P<pk>\d+)/$', views.StudentDetailView.as_view(), name='detail'),
#     url(r'add/$', views.StudentCreateView.as_view(), name='add'),
#     url(r'edit/(?P<pk>\d+)/$', views.StudentUpdateView.as_view(), name='edit'),
#     url(r'remove/(?P<pk>\d+)/$', views.StudentDeleteView.as_view(), name='remove'),
# ]
