from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
from .models import Task, Category, Priority, Note, SubTask
from .forms import TaskForm, CategoryForm, PriorityForm, NoteForm, SubTaskForm

# Authentication Views
def custom_login(request):
    if request.method == 'POST':
        # Simple session-based login (for demo)
        request.session['is_authenticated'] = True
        request.session['username'] = request.POST.get('username', 'User')
        return redirect('home')
    return render(request, 'login.html')

def custom_logout(request):
    logout(request)
    if 'is_authenticated' in request.session:
        del request.session['is_authenticated']
    if 'username' in request.session:
        del request.session['username']
    return redirect('login')

def github_login_demo(request):
    """Demo view for GitHub login"""
    username = f"github_user_{random.randint(1000, 9999)}"
    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'email': f'{username}@example.com', 
            'first_name': 'GitHub',
            'last_name': 'User'
        }
    )
    login(request, user)
    return redirect('home')

# Main Views
def home(request):
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status='completed').count()
    pending_tasks = Task.objects.filter(status='pending').count()
    
    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'username': request.session.get('username', 'User'),
        'is_authenticated': request.session.get('is_authenticated', False)
    }
    return render(request, 'home.html', context)

# Task Views
def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'is_authenticated': request.session.get('is_authenticated', False)
    }
    return render(request, 'task_list.html', context)

def task_add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form, 'title': 'Add Task'})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form, 'title': 'Edit Task'})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'task_delete.html', {'task': task})

# Category Views
def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'is_authenticated': request.session.get('is_authenticated', False)
    }
    return render(request, 'category_list.html', context)

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form, 'title': 'Add Category'})

def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form, 'title': 'Edit Category'})

def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('category_list')
    return render(request, 'category_delete.html', {'category': category})

# Priority Views
def priority_list(request):
    priorities = Priority.objects.all()
    context = {
        'priorities': priorities,
        'is_authenticated': request.session.get('is_authenticated', False)
    }
    return render(request, 'priority_list.html', context)

# Note Views
def note_list(request):
    notes = Note.objects.all()
    context = {
        'notes': notes,
        'is_authenticated': request.session.get('is_authenticated', False)
    }
    return render(request, 'note_list.html', context)

def note_add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note created successfully!')
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form, 'title': 'Add Note'})

def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully!')
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form, 'title': 'Edit Note'})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully!')
        return redirect('note_list')
    return render(request, 'note_delete.html', {'note': note})

# SubTask Views
def subtask_list(request):
    subtasks = SubTask.objects.all()
    context = {
        'subtasks': subtasks,
        'is_authenticated': request.session.get('is_authenticated', False)
    }
    return render(request, 'subtask_list.html', context)

def subtask_add(request):
    if request.method == 'POST':
        form = SubTaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SubTask created successfully!')
            return redirect('subtask_list')
    else:
        form = SubTaskForm()
    return render(request, 'subtask_form.html', {'form': form, 'title': 'Add SubTask'})

def subtask_edit(request, pk):
    subtask = get_object_or_404(SubTask, pk=pk)
    if request.method == 'POST':
        form = SubTaskForm(request.POST, instance=subtask)
        if form.is_valid():
            form.save()
            messages.success(request, 'SubTask updated successfully!')
            return redirect('subtask_list')
    else:
        form = SubTaskForm(instance=subtask)
    return render(request, 'subtask_form.html', {'form': form, 'title': 'Edit SubTask'})

def subtask_delete(request, pk):
    subtask = get_object_or_404(SubTask, pk=pk)
    if request.method == 'POST':
        subtask.delete()
        messages.success(request, 'SubTask deleted successfully!')
        return redirect('subtask_list')
    return render(request, 'subtask_delete.html', {'subtask': subtask})