from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blocks.models import Title, Block_3, Block_4, Block_5, Block_6
# Create your views here.

class TitleView(ListView):
    model = Title
    template_name = 'blocks/header.html'
    context_object_name = 'blocks'


def index(request):
    return render(request, "index.html")