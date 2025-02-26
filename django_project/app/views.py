from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.views import LoginView

from app.models import Task

class TaskList(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(deleted_at__isnull=True)

class TaskDetail(DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"

class TaskCreate(CreateView):
    model = Task
    template_name = "task_add_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("app:task_list")

class TaskUpdate(UpdateView):
    model = Task
    template_name = "task_edit_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("app:task_list")

class TaskDelete(DeleteView):
    model = Task
    template_name = "task_delete_confirm.html"
    success_url = reverse_lazy("app:task_list")

    def form_valid(self, form):
        self.object.delete()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = "login.html"