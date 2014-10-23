from django.db import models


class AbstractTasks (models.Model):
    abstract_task = models.TextField()
    related_cards_url = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=4)


class ConcreteTasks (models.Model):
    concrete_task = models.TextField()
    related_cards_url = models.CharField(max_length=50)
    correct_answer = models.CharField(max_length=4)


class Subjects (models.Model):
    subject = models.CharField(max_length=30)
    subject_group = models.CharField(max_length=10)


class Answers (models.Model):
    answer = models.CharField(max_length=1)
    subject = models.ForeignKey(Result, related_name='answers')
    
