from django.urls import path
from .views import HomeTemplateView
from django.conf.urls import url
from core import views


app_name = 'core'


urlpatterns = [
    path('', HomeTemplateView.as_view()),
    url(r'^home$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    path('allblogs/', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name="detail"),
]
