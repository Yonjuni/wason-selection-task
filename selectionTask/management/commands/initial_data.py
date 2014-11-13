from django.core.management import BaseCommand
from django.db import transaction
from selectionTask.models import AbstractTask, ConcreteTask
import json
import os


@transaction.atomic
def create_initial_data():
    with open(os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                os.path.pardir,
                os.path.pardir,
                os.path.pardir,
                "sample_data.json")),
              'r') as data_file:
        data = json.loads(data_file.read())
        for task_data in data['abstractTasks']:
            task = AbstractTask()
            task.description = task_data['description']
            task.first_card = task_data['firstCard']['card']
            task.first_card_should_flip = task_data['firstCard']['isFlipped']
            task.second_card = task_data['secondCard']['card']
            task.second_card_should_flip = task_data['secondCard']['isFlipped']
            task.third_card = task_data['thirdCard']['card']
            task.third_card_should_flip = task_data['thirdCard']['isFlipped']
            task.fourth_card = task_data['fourthCard']['card']
            task.fourth_card_should_flip = task_data['fourthCard']['isFlipped']
            task.story = task_data['story']
            task.save()
        print("Abstract tasks loaded ...")
        for task_data in data['concreteTasks']:
            task = ConcreteTask()
            task.description = task_data['description']
            task.first_card = task_data['firstCard']['card']
            task.first_card_should_flip = task_data['firstCard']['isFlipped']
            task.second_card = task_data['secondCard']['card']
            task.second_card_should_flip = task_data['secondCard']['isFlipped']
            task.third_card = task_data['thirdCard']['card']
            task.third_card_should_flip = task_data['thirdCard']['isFlipped']
            task.fourth_card = task_data['fourthCard']['card']
            task.fourth_card_should_flip = task_data['fourthCard']['isFlipped']
            task.story = task_data['story']
            task.save()
        print("Concrete tasks loaded ...")



class Command(BaseCommand):
    args = ''
    help = 'Creates initial task data in the database'


    def handle(self, *args, **options):
        self.stdout.write("Creating initial task data ...\n")
        create_initial_data()
        self.stdout.write("Done loading initial task data ...\n")