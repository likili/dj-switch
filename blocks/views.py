from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return render(request, "index.html")