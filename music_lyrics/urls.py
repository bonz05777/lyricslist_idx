# music_lyrics/urls.py
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import LyricsViewSet

router = DefaultRouter()
router.register(r'api/lyrics', LyricsViewSet)  # Registers all CRUD API endpoints


urlpatterns = [
    path('', views.lyrics_list, name='lyrics_list'),
    path('lyrics/<int:pk>/', views.lyrics_detail, name='lyrics_detail'),  # New detail view
    path('lyrics/create/', views.lyrics_create, name='lyrics_create'),
    path('lyrics/<int:pk>/update/', views.lyrics_update, name='lyrics_update'),
    path('lyrics/<int:pk>/delete/', views.lyrics_delete, name='lyrics_delete'),
    path('about/', views.about, name='about'),  
    path('', include(router.urls)),
   
]
