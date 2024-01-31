# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    
    
@csrf_exempt
@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            response_data = {
                'status': 'success',
                'content': comment.content,
                'author': comment.author.username
            }
            return JsonResponse(response_data)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'status': 'error', 'errors': errors})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})