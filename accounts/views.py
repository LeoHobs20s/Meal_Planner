from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm

def login_view(request):
    """ This view will render the login form """

    if request.method == 'POST':
        # POST Data Submitted; process data
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        # No Data Submitted; create blank form
        form = LoginForm()
    
    context = {'form':form}
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    """ This view will render the logout system """

    logout(request)
    return redirect('login_view')


def register(request):
    """ This view will render the loog """

    if request.method == 'POST':
        # POST Data Submitted; process data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            user = authenticate(username=new_user.username, password=request.POST['password1'])
            if user is not None:
                # logging in new user
                login(request, user)
                return redirect('home')
    else:
        # No Data Submitted; create blank form
        form = UserCreationForm()
    
    context = {'form':form}
    return render(request, 'accounts/register.html', context)