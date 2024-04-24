from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
# Create your views here.

class ListaPendientes(ListView):
    model = Task
    context_object_name = 'tasks'

class DetalleTarea(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html' # esto es para buscar directamente el template con el nombre que le hayamos asignado a la pagina hmtl

class CreateTask(CreateView):
    model = Task
    fields = '__all__' # esto es para agregar todos los contenidos para crear el formulario dentro del models.py Task
    success_url = reverse_lazy('tasks')

class EditTask(UpdateView):
    model = Task
    fields = '__all__'  # esto es para agregar todos los contenidos para crear el formulario dentro del models.py Task
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
