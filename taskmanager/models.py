from django.db import models
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)  # only auto_now_add
    updated_at = models.DateTimeField(auto_now=True)      # only auto_now

    class Meta:
        abstract = True

# Category model
class Category(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


# Priority model
class Priority(BaseModel):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name

# Task model
class Task(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    def __str__(self):
        return self.title

class SubTask(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")

    def __str__(self):
        return self.title

    def parent_task_name(self):
        return self.parent_task.title

class Note(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="notes")
    content = models.TextField()

    def __str__(self):
        return f"Note for {self.task.title}"
