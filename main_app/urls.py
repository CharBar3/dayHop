from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post_index, name='posts_index'),
    path('post/<int:post_id>/', views.post_detail, name='posts_detail'),
    path('post/create/', views.PostCreate.as_view(), name='posts_create'),
    path('post/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('date/<int:post_id>/', views.date, name='date'),
    path('accounts/signup/', views.signup, name='signup'),
]
