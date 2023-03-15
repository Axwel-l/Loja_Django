from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView ,
    )
from django.views.generic import  ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from produtos.models import Categoria
# Create your views here.

@login_required
def index(request):
    return HttpResponse('Ola Django(index)')

def ola(request):
    return HttpResponse('Ola Django')

class CreateCategoryView(LoginRequiredMixin, CreateView):
    model=Categoria
    fields=('name','description')
    template_name= 'create_category.html'
    success_url = reverse_lazy('list_category')

class ListCategoryView(ListView):
    model = Categoria
    template_name = 'list_category.html'
    context_object_name='categories'

class DetailCategoryView(DetailView):
    model = Categoria
    template_name= 'category_detail.html'

class UpdateCategoryView(LoginRequiredMixin ,UpdateView):
    model =Categoria
    template_name= 'category_form.html'
    fields=('name','description')
    success_url = reverse_lazy('list_category')
class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model =Categoria
    template_name='category_delete.html'
    success_url = reverse_lazy('list_category')
