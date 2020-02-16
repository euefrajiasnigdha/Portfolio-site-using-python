from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^special/', views.special, name='special'),
    url(r'^core/', include('core.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('allblogs/', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name="detail"),



                  # include our custom app urls here
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
