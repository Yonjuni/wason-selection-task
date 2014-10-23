from django.db import models


class ControlTasks (models.Model):
    control_task = models.TextField()
    related_cards_url = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=4)


class Tasks (models.Model):
    task = models.TextField()
    related_cards_url = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=4)


class Subjects (models.Model):
    subject = models.CharField(max_length=30)
    subject_group = models.CharField(max_length=10)


class Answers (models.Model):
    answer = models.CharField(max_length=1)
    subject = models.ForeignKey(Result, related_name='answers')
    
