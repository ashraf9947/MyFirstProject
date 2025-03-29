from django.contrib import admin
from django.urls import path, include  # ✅ Убедись, что импортирован include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # ✅ Добавь эту строку
]
