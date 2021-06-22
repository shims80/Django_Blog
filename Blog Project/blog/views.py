from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django .views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .views import *
from .models import Post,Comment
from django.urls import reverse_lazy, reverse
from .forms import *
from django.db.models import Q

from operator import attrgetter


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_queryset(self):
        qs = Post.objects.all().order_by("-date_posted")
        query = self.request.GET.get("q")
        if query:
            
            blog_posts = sorted(get_blog_queryset(query),key=attrgetter('date_posted'), reverse=True)
            qs = blog_posts
        return qs


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_query_set(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content','header_image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content','header_image']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def chat(request):
    return render(request, 'blog/chat.html', {'title': 'chat'})

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


def get_blog_queryset(query = None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = Post.objects.filter(
                Q(title__icontains=q)|
                Q(content__icontains=q)|
                Q(date_posted__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)
    return list(set(queryset))


