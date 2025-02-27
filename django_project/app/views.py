from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from app.models import Task


class TaskList(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        # ログインユーザーのタスクのみを取得
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user, deleted_at__isnull=True)
        return Task.objects.filter(deleted_at__isnull=True)


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task_detail.html"
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task_add_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("app:task_list")

    def form_valid(self, form):
        # ログインユーザーをタスクのユーザーに設定
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task_edit_form.html"
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("app:task_list")


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task_delete_confirm.html"
    success_url = reverse_lazy("app:task_list")

    def form_valid(self, form):
        self.object.delete()
        return super().form_valid(form)


class TaskListLoginView(LoginView):
    template_name = "task_login.html"
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("app:task_list")


class TaskListLogoutView(LogoutView):
    next_page = reverse_lazy("app:login")


class UserRegisterView(FormView):
    template_name = "user_register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("app:task_list")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class TaskListSearch(ListView):
    model = Task
    template_name = "task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        search_query = self.request.GET.get("search", "").strip()
        queryset = Task.objects.filter(user=self.request.user, deleted_at__isnull=True)

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset
