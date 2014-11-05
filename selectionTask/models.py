from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Task (models.Model):
    description = models.TextField()
    first_card = models.CharField(max_length=20)
    second_card = models.CharField(max_length=20)
    third_card = models.CharField(max_length=20)
    fourth_card = models.CharField(max_length=20)
    first_card_should_flip = models.BooleanField()
    second_card_should_flip = models.BooleanField()
    third_card_should_flip = models.BooleanField()
    fourth_card_should_flip = models.BooleanField()
    story = models.TextField()

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
    subject_id = models.CharField('Subject ID', max_length=30, unique=True, editable=False)
    group = models.BooleanField('is abstract group', editable=False)

    def __unicode__(self):
        return 'Subject: ' + self.subject_id

    def is_abstract_group (self):
        return self.group

    def is_concrete_group (self):
        return not self.group


class Result (models.Model):
    subject = models.ForeignKey(Subject, related_name='results', editable=False)
    task = models.ForeignKey(Task, related_name='results', editable=False)
    first_card_flipped = models.BooleanField(editable=False)
    second_card_flipped = models.BooleanField(editable=False)
    third_card_flipped = models.BooleanField(editable=False)
    fourth_card_flipped = models.BooleanField(editable=False)

    def __unicode__(self):
        return 'Result No. ' + str(self.id) + ' of ' + str(self.subject)
