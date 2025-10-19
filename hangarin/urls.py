from django.contrib import admin
from django.urls import path, include
from taskmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('auth/github/', views.github_login_demo, name='github_login'),
    path('', views.home, name='home'),
    
    # Tasks
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.task_add, name='task_add'),
    path('tasks/<int:pk>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    
    # Categories
    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.category_add, name='category_add'),
    path('categories/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('categories/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # Priorities
    path('priorities/', views.priority_list, name='priority_list'),

    # Notes
    path('notes/', views.note_list, name='note_list'),
    path('notes/add/', views.note_add, name='note_add'),
    path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
    
    # SubTasks
    path('subtasks/', views.subtask_list, name='subtask_list'),
    path('subtasks/add/', views.subtask_add, name='subtask_add'),
    path('subtasks/<int:pk>/edit/', views.subtask_edit, name='subtask_edit'),
    path('subtasks/<int:pk>/delete/', views.subtask_delete, name='subtask_delete'),
]