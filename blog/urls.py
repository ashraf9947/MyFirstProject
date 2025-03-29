from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='home'),  # Главная страница с постами
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),  # Страница отдельного поста
]
