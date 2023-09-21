from django.urls import path
from .views import create_blog, all_blogs, blog_detail, update_blog, delete_blog

urlpatterns = [
   path('create/',create_blog, name='create-blog'),
   path('',all_blogs, name='all_blogs'),
   path('blog/<int:pk>/',blog_detail, name='blog-detail'),
   path('blog/update/<int:pk>/',update_blog, name='update-blog'),
   path('blog/delete/<int:pk>/',delete_blog, name='delete_blog'),
]