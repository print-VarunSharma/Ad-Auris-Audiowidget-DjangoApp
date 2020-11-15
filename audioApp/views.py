from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from django.db import models

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.template import Context, loader, TemplateDoesNotExist
from django.http import Http404

from django.views.generic import TemplateView

from audioApp import views

# Create your views here.
class audioWidgetTest(TemplateView):
    template_name = 'widget_analytics.html'

    def widgetTest(request):
        return render(request, 'widget_analytics.html', context)

class IndexView(View):
    template_name = 'index.html'
    
    def index(request):
        return render(request, 'index.html', context)

class rebit_2(TemplateView):
    template_name = 'widget_analytics.html'

    def rebit_2(request):
        return render(request, 'rebit_2.html', context)

class Home(TemplateView):
    template_name = 'home.html'

    def home(request):
        return render(request, 'home.html', context)
