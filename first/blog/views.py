from django.shortcuts import render
from .models import Post
from django.utils import timezone
import subprocess
from blog.python1 import sum
from django.template.context_processors import csrf

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts':posts}) 

def button(request):
    if request.method == 'POST':
        #subprocess.check_call(['python', 'python1.py'])
        val = sum()
        print(val)
    return render(request, "blog/file.html", {"val":val})    
