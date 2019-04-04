from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect


def home(request):
    return render(request,'home/home.html')


# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=user.email, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# Create your views here.
