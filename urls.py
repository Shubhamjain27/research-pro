from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
app_name = 'signup'


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^signup2/$', views.signup_student, name='signup2'),
    url(r'^$', views.home, name='home'),
    url(r'^intern/$', views.internview, name='InternForm'),
    url(r'^student/$', views.home2, name='home2'),
    url(r'^login/$', auth_views.login, {'template_name': 'signup/login.html'}, name='login'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard2/$', views.dashboard2, name='dashboard2'),
    url(r'^projects/$', views.Projects.as_view(), name='projects'),
    url(r'^projects/(?P<pk>\d+)$', views.ProjectsDetail.as_view(), name='detail'),
    url(r'^projects/apply/(?P<pk>\d+)$', views.apply, name='apply'),
    url(r'^projects/apply2/(?P<pk>\d+)$', views.change_friends, name='change_friends2'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'signup/logout.html'}, name='logout'),
]