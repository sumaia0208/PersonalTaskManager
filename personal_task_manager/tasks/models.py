from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# This is Task database table.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    # status P means Pending, C means Completed etc
    status = models.CharField(max_length=1, default="P")
    # when created instance, this time automatically create time. so use auto_now_add
    created_at = models.DateTimeField(auto_now_add=True)
    # when update instance time will update so auto_now
    updated_at = models.DateTimeField(auto_now=True)

    def check_status(self):
        current_date = datetime.now().date()

        if current_date > self.due_date:
            self.status = "C"
        elif current_date < self.due_date:
            self.status = "P"
        return self.status

    def __str__(self):
        return self.title
