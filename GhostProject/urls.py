"""GhostProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GhostProject import views
from GhostProject.models import Post
from django.conf import settings
from django.conf.urls.static import static

admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='homepage'),
    path('addpost/', views.addpostview, name="addpost"),
    path('boasts/', views.boasts, name='boasts'), 
    path('roasts/', views.roasts, name='roasts'),
    path('upvote/<int:id>', views.upvoting, name='upvoted'),
    path('downvote/<int:id>', views.downvoting, name='downvoted'),
    path('netvotes/', views.netvotes, name='votes'),
    path('delete/<int:id>', views.delete_post, name='delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
