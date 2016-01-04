from django.shortcuts import render, redirect
from users.forms import UserForm
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout


# Create your views here.
class Welcome(View): 
    def get(self,request):
        return render(request, 'users/welcome.html', {'form': {'login':
        UserForm(), 'register': UserForm()}})

class Login_(View):
    def post(self,request):
        user_form = UserForm(request.POST)
        username = user_form['username'].value()
        password = user_form['password'].value()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user_id'] = username
                return redirect('users:welcome')
        return render(request, 'users/welcome.html', {'form':
            {'login': user_form, 'register': UserForm()}} )


class Create_user(View): 
    def get(self,request): 
        return render(request, 'users/create_user.html', {'form':UserForm()})


class Register(View): 
    def post(self,request): 
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            raw_pass = user.password
            user.password = make_password(user.password)
            user.save()
            user = authenticate(username=user.username, password=raw_pass)
            if user is not None:
                if user.is_active:
                    request.session['user_id'] = user.username
                    login(request, user)
                    return redirect('users:welcome')
        return render(request, 'users/welcome.html', {'form':
            {'login': UserForm(), 'register': user_form}} )



