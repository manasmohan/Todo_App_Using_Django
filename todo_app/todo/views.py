from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Tasks, Register, Login
from .forms import RegisterForm, LoginForm


# Create your views here.


class TaskList(ListView):
    model = Tasks
    context_object_name = 'task'
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task')
    template_name = 'taskcreate.html'


class TaskDelete(DeleteView):
    model = Tasks
    context_object_name = 'task'
    success_url = reverse_lazy('task')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'task_detail.html'


def register_fun(request):
    register = Register.objects.all()
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    context = {'register': register, 'form': form}
    return render(request, 'register.html', context)


def login_fun(request):
    login = Login.objects.all()
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('task')
    context = {'login': login, 'form': form}
    return render(request, 'login.html', context)
