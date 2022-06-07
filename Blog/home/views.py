from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            
            BlogModel.objects.create(
                user=user, title=title, image=image,content=content,
            )

            return redirect('/')

    except Exception as e:
        print(e)
    return render(request, 'add_blog.html', context)

def register_view(request):
    return render(request, 'register.html')