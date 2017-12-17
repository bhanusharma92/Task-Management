from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, SignInForm, AddTaskForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Task, Label
import datetime


def index(request):
    return render(request, 'task/index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            request.session['username'] = user.username
            return HttpResponseRedirect(reverse('task:after_login'))
    else:
        form = SignUpForm()

    return render(request, 'task/sign_up.html', {'form': form})


def after_login(request):
    username = request.session['username']
    return render(request, 'task/after_login.html', {'username': username})


def sign_in(request):
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                request.session['username'] = user.username
                return HttpResponseRedirect(reverse('task:after_login'))
            else:
                form = SignInForm()
    return render(request, 'task/sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    request.session.clear()
    return HttpResponseRedirect(reverse('task:index'))


def add_task(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    form = AddTaskForm()
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            task_name = form.cleaned_data['task_name']
            task_description = form.cleaned_data['task_description']
            expiry_date = form.cleaned_data['expiry_date']
            label = form.cleaned_data['label']
            priority = form.cleaned_data['priority']
            task = Task(name=task_name,
                        description=task_description,
                        date_created=datetime.datetime.now(),
                        last_updated=datetime.datetime.now(),
                        expiry=expiry_date,
                        label=label,
                        priority=priority,
                        user=user)
            task.save()
            return HttpResponseRedirect(reverse('task:view_task'))
    return render(request, 'task/add_task.html', {'form': form})


def view_task(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    tasks = Task.objects.filter(user=user, is_deleted=False)
    return render(request, 'task/view_task.html', {'tasks': tasks})


def delete_task(request):
    username = request.session['username']
    user = User.objects.get(username=username)
    tasks = Task.objects.filter(user=user, is_deleted=False)
    if request.method == 'POST':
        task_id = request.POST.getlist('task_id')
        print(type(task_id))
        for t in task_id:
            tasks_to_delete = Task.objects.get(id=t)
            tasks_to_delete.is_deleted = True
            tasks_to_delete.save()
    return render(request, 'task/delete_task.html', {'tasks': tasks})
