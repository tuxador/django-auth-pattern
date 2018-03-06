#!python
# authtest/urls.py
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from log.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('log.urls')),
    url(r'^login/$', views.login, {'template_name': 'login.html',
                                   'authentication_form': LoginForm},
        name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/login'}),  
]

# urlpatterns = [
#     path('index/', views.index, name='main-view'),
#     path('bio/<username>/', views.bio, name='bio'),
#     path('articles/<slug:title>/', views.article, name='article-detail'),
#     path('articles/<slug:title>/<int:section>/', views.section, name='article-section'),
#     path('weblog/', include('blog.urls')),
#     ...
# ]
