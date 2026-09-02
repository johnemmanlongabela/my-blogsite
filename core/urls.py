from django.contrib import admin
from django.urls import path
from django_distill import distill_path
from blog import views
from blog.models import Post

def get_all_posts():
    for post in Post.objects.all():
        yield {'slug': post.slug}

urlpatterns = [
    path('admin/', admin.site.urls),
    distill_path('my-blogsite/', views.post_list, name='post_list'),
    distill_path('my-blogsite/<slug:slug>/', views.post_detail, name='post_detail', distill_func=get_all_posts),
]