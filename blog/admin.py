from django.contrib import admin
from blog.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def log_change(self, request, object, message):
        pass  

@admin.register(Comment)  # Добавляем комментарии в Django Admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_on', 'active')  # Показываем в таблице
    list_filter = ('active', 'created_on')  # Добавляем фильтрацию
    search_fields = ('name', 'body')  # Поле поиска
    actions = ['approve_comments']  # Действие "одобрить комментарий"

    def approve_comments(self, request, queryset):
        queryset.update(active=True)  # Одобрение комментариев
