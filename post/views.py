from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def posts(request):
    content = Post.objects.all()
    return render(request=request, context={'content': content}, template_name='design.html')