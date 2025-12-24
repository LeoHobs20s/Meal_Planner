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


