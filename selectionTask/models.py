from django.db import models


class AbstractTask (models.Model):
    description = models.TextField()
    card_one = models.CharField(max_length=10)
    card_two = models.CharField(max_length=10)
    card_three = models.CharField(max_length=10)
    card_four = models.CharField(max_length=10)
    card_one_isflipped = models.BooleanField()
    card_two_isflipped = models.BooleanField()
    card_three_isflipped = models.BooleanField()
    card_four_isflipped = models.BooleanField()


class ConcreteTask (models.Model):
    description = models.TextField()
    card_one = models.CharField(max_length=10)
    card_two = models.CharField(max_length=10)
    card_three = models.CharField(max_length=10)
    card_four = models.CharField(max_length=10)
    card_one_isflipped = models.BooleanField()
    card_two_isflipped = models.BooleanField()
    card_three_isflipped = models.BooleanField()
    card_four_isflipped = models.BooleanField()


class Subject (models.Model):
    subject_id = models.CharField(max_length=30, unique=True)
    group = models.BooleanField()

    def is_abstract_group (self):
        return self.group

    def is_concrete_group (self):
        return not self.group


class Result (models.Model):
    subject = models.ForeignKey(Subject, related_name='results')
    card_one_isflipped = models.BooleanField()
    card_two_isflipped = models.BooleanField()
    card_three_isflipped = models.BooleanField()
    card_four_isflipped = models.BooleanField()
