from django.urls import path 
from .views import blog_list, blog_detail,blog_delete,blog_create,blog_update, PostListCreateView, PostDetailView


urlpatterns = [ 
    path('',blog_list), 
    path('create/', blog_create),
    path('<id>/update', blog_update),
    path('<id>/',blog_detail), 
    path('<id>/delete',blog_delete), 
   # For the API views with simplified paths
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    ]

    