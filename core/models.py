from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model() 

class Project(models.Model):
    name = models.CharField(max_length=255) # name field 
    description = models.TextField() # decription field 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects') # owner field with auto delete projects when user is deleted
    created_at = models.DateTimeField(auto_now_add=True) # timestamp for when the project is created
    updated_at = models.DateTimeField(auto_now=True) # timestamp for when the project is updated 

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255) # title field
    priority = models.CharField(max_length=10, choices=[('low', 'Low'),('medium', 'Medium'),('high', 'High')],default='medium')
    description = models.TextField() # description field
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks') # project field with auto delete tasks when project is deleted
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks') # assigned_to field with auto set to null when user is deleted
    due_date = models.DateField(null=True, blank=True) # due_date field

    STATUS_CHOICES = [('pending', 'Pending'), ('in_progress', 'In Progress'),('completed', 'Completed') ]  # projects status 
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending') # status field with default value of pending
    
    created_at = models.DateTimeField(auto_now_add=True) # timestand for when the task is created
    updated_at = models.DateTimeField(auto_now=True) # timestamp for when the task is updated 

    def __str__(self):
        return self.title   

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments') # task field with auto delete comments when task is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments') # author field with auto delete comments when user is deleted
    body = models.TextField() #textfield for the comment body
    created_at = models.DateTimeField(auto_now_add=True) # timestamp for when the comment is created
    updated_at = models.DateTimeField(auto_now=True) # timestamp for when the comment is updated

    def __str__(self):
        return f'Comment by {self.author.username} on {self.task.title}'