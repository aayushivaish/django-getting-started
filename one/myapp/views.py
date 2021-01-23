from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import short_url
from .forms import UrlForm
from .short import shortner
# Create your views here.
def make(request, token):
    long_url = short_url.objects.filter(short_url = token )[0]
    return redirect(long_url.long_url)
@login_required
def index(request):
    abc = short_url.objects.filter(user = request.user).values
    form  = UrlForm(request.POST)
    a = ''
    myurl = ''
    if request.method == 'POST':
        if form.is_valid():
            newurl = form.save(commit = False)
            a = shortner().issue_token()
            newurl.short_url = a
            newurl.user = request.user
            newurl.save()
            myurl = 'http://127.0.0.1:8000/' + a
        else:
            form = UrlForm()
            a = 'invalid url'
    return render(request,"index.html", {'form':form,'a':myurl,'abc': abc})




class signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
    

    
    
