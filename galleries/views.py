from django.shortcuts import render, redirect
from galleries.models import gallery, gallerytype
from django.core.paginator import Paginator, EmptyPage
from math import ceil
from django.views.generic import ListView, DetailView
from django.views import View
from django.http import Http404
from . import forms
from users.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
# Create your views here.


'''
def gallery_detail(request, pk):

    try:
        gallery_pk = gallery.objects.get(pk=pk)
    except gallery.DoesNotExist:
        raise Http404()
    return render(request, "galleries/detail.html" ,context={"gallery_pk": gallery_pk})

'''
'''

def SearchView(request):

    
    galtype = request.GET.get("gallery_type")
    print(galtype)
    galleries = gallery.objects.all()
    filter_args = {}
    filter_args["gallery_type__name__exact"] = galtype
    galleries = gallery.objects.filter(**filter_args)
    return render(request, "search.html", context={"gal":galleries})
    

    name = request.GET.get("name")
    if name is None:
        form = forms.GalleryForm()
        
    else:    
        form = forms.GalleryForm(request.GET)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            gallery_type = form.cleaned_data.get("gallery_type")
            filter_args = {}
            if name is not None:
                filter_args["name"] = name
            if gallery_type != "nothing":
                filter_args['gallery_type'] = gallery_type
            galleries = gallery.objects.filter(**filter_args)

            return render(request, "search.html", context = {"form":form, "galleries":galleries})

    return render(request, "search.html", context = {"form":form})
'''

class LoginView(View):

    def get(self, request):
        form = forms.LoginForm()
        return render(request, "login.html", context={"form":form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username=email,password=password)
            if user is not None:
                login(request, user)
                print("here")
                return redirect(reverse("home:front"))
        return render(request, "login.html", context={"form":form})


def log_out(request):
    logout(request)
    return redirect(reverse("home:front"))