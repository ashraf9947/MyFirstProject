from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView
from .models import Post, Comment
from .forms import CommentForm

# Представление для главной страницы (список постов)
class PostList(ListView):
    model = Post
    template_name = 'index.html'  # Убедитесь, что этот файл существует
    context_object_name = 'posts'
    ordering = ['-created_on']

# Представление для детальной страницы поста
class PostDetail(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        form = CommentForm()
        return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': form})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = post.comments.filter(active=True)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', slug=post.slug)  # Перенаправление после добавления комментария

        return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': form})
