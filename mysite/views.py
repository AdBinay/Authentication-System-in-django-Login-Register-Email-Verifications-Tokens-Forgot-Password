from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django import forms
from django.shortcuts import redirect, render


class RegisterationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

def registration_view(request):
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request , user)
            return redirect("index")
    else:
        form = RegisterationForm()

    return render(request, "registration/register.html", {"form":form})
    
def index(request):
    return render(request, "index.html")