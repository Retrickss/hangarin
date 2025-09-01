from django.db import models

# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Priority model
class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Task model
class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=50,
        choices=[
            ("Pending", "Pending"),
            ("In Progress", "In Progress"),
            ("Completed", "Completed"),
        ],
        default="Pending"
    )

    def __str__(self):
        return self.title
