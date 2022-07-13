from django.shortcuts import redirect, render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def post_index(request):
    posts = Post.objects.filter(user=request.user)
    if len(posts) == 0:
        no_posts = True
    else: 
        no_posts = False
    return render(request, 'post/index.html', {'posts': posts, 'no_posts': no_posts})

@login_required
def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post/detail.html', {'post': post})

@login_required
def date(request, post_id):
    post = Post.objects.get(id=post_id)
    posts = Post.objects.filter(
        user=request.user,
        date__month=post.date.month, 
        date__day=post.date.day)
    day = (f'{posts[0].date.strftime("%B")} {posts[0].date.day}')
    return render(request, 'post/date.html', {'posts': posts, 'day': day})

def signup(request):
    error_messages = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_messages = 'Invalid Info - Please Try Again'
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error_messages': error_messages
    })


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['date', 'title', 'body']
    success_url = '/post'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['date', 'title', 'body']


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/post'

