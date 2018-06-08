from django.shortcuts import render
from django.http import HttpResponse
from mousehouse.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import forms
from .forms import UserRegistrationForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def index(request):
    return render(request, 'index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

@login_required
def view_post(request, slug):
    post_types = {
        1: 'mousehouse.view_pg',
        2: 'mousehouse.view_adult',
        3: 'mousehouse.view_adult_plus',
        4: 'mousehouse.view_standard'
    }
    post = get_object_or_404(Blog, slug=slug)
    permissions = list(request.user.get_group_permissions())
    
    if post_types[post.permission_type] in permissions:
        return render(request, 'view_post.html', {
            'post': post
        })
    else:
        return render(request, 'not_permitted.html')

@login_required
def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                standard_group = Group.objects.get(name='standard')
                standard_group.user_set.add(user) 
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})