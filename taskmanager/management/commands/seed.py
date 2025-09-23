from django.core.management.base import BaseCommand
from faker import Faker
import random
from django.utils import timezone
from taskmanager.models import Task, SubTask, Note, Category, Priority

fake = Faker()

class Command(BaseCommand):
    help = "Seed database with fake Tasks, SubTasks, and Notes"

    def handle(self, *args, **kwargs):
        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        if not priorities or not categories:
            self.stdout.write(self.style.ERROR(
                "⚠️ Please add Priorities (High, Medium, Low, Critical, Optional) "
                "and Categories (Work, School, Personal, Finance, Projects) manually first!"
            ))
            return

        # Create 10 fake tasks
        for _ in range(10):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                priority=random.choice(priorities),
                category=random.choice(categories),
            )

            # Add 2 subtasks for each task
            for _ in range(2):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=3),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                    parent_task=task,
                )

            # Add 2 notes for each task
            for _ in range(2):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2),
                )

        self.stdout.write(self.style.SUCCESS("🎉 Fake data (Tasks, SubTasks, Notes) generated successfully!"))
