from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Task (models.Model):
    description = models.TextField()
    card_one = models.CharField(max_length=20)
    card_two = models.CharField(max_length=20)
    card_three = models.CharField(max_length=20)
    card_four = models.CharField(max_length=20)
    card_one_isflipped = models.BooleanField()
    card_two_isflipped = models.BooleanField()
    card_three_isflipped = models.BooleanField()
    card_four_isflipped = models.BooleanField()
    story = models.TextField(default='', blank=True)

    def __unicode__(self):
        try:
            self.concretetask
            self.__class__ = ConcreteTask
        except ObjectDoesNotExist:
            self.__class__ = AbstractTask
        return str(self)


class AbstractTask (Task):
    def __unicode__(self):
        return 'Abstract Task: ' + str(self.id)


class ConcreteTask (Task):
    def __unicode__(self):
        return 'Concrete Task: ' + str(self.id)


class Subject (models.Model):
    subject_id = models.CharField(max_length=30, unique=True)
    group = models.BooleanField()

    def __unicode__(self):
        return 'Subject: ' + self.subject_id

    def is_abstract_group (self):
        return self.group

    def is_concrete_group (self):
        return not self.group


class Result (models.Model):
    subject = models.ForeignKey(Subject, related_name='results')
    task = models.ForeignKey(Task, related_name='results')
    first_card_flipped = models.BooleanField()
    second_card_flipped = models.BooleanField()
    third_card_flipped = models.BooleanField()
    fourth_card_flipped = models.BooleanField()

    def __unicode__(self):
        return 'Result No. ' + str(self.id) + ' of ' + str(self.subject)
