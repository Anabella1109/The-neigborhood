from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm, Profileform, Postform
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Post
from django.contrib.auth.models import User
@login_required(login_url='/accounts/login/')
def home(request):
    user=request.user
    profile=Profile.objects.get(user=user)
    posts=Post.objects.all()
    neighbors=Profile.objects.filter(neighborhood=profile.neighborhood)
    return render(request, 'home/home.html',{'posts':posts,'neighbors':neighbors,'profile':profile})



@login_required(login_url='/accounts/login/')
def edit_profile(request,edit):
    current_user = request.user
    profile=Profile.objects.get(user=current_user)
    
   
    if request.method == 'POST':
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            
            profile.bio=form.cleaned_data['bio']
            profile.photo = form.cleaned_data['photo']
            profile.first_name = form.cleaned_data['first_name']
            profile.last_name = form.cleaned_data['last_name']
            profile.phone_number = form.cleaned_data['phone_number']
            profile.neighborhood = form.cleaned_data['neighborhood']
            profile.user=current_user

            
            profile.save()
        return redirect('home')

    else:
        form = Profileform()
    return render(request, 'edit_profile.html', {"form": form , 'user':current_user})

@login_required(login_url='/accounts/login/')
def profile(request,id):
     user=User.objects.get(id=id)
     profile=Profile.objects.get(user=user)
     
     
     return render(request, 'profile.html',{"user":user,"profile": profile})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.profile=profile
            post.save()
        return redirect('home')

    else:
        form = Postform()
    return render(request, 'new_post.html', {"form": form})
     



# Create your views here.
