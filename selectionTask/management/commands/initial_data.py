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
                "initial_data.json")),
              'r') as data_file:
        data = json.loads(data_file.read())
        for task_data in data['abstractTasks']:
            task = AbstractTask()
            task.description = task_data['description']
            task.card_one = task_data['firstCard']['card']
            task.card_one_isflipped = task_data['firstCard']['isFlipped']
            task.card_two = task_data['secondCard']['card']
            task.card_two_isflipped = task_data['secondCard']['isFlipped']
            task.card_three = task_data['thirdCard']['card']
            task.card_three_isflipped = task_data['thirdCard']['isFlipped']
            task.card_four = task_data['fourthCard']['card']
            task.card_four_isflipped = task_data['fourthCard']['isFlipped']
            task.save()
        print("Abstract tasks loaded ...")
        for task_data in data['concreteTasks']:
            task = ConcreteTask()
            task.description = task_data['description']
            task.card_one = task_data['firstCard']['card']
            task.card_one_isflipped = task_data['firstCard']['isFlipped']
            task.card_two = task_data['secondCard']['card']
            task.card_two_isflipped = task_data['secondCard']['isFlipped']
            task.card_three = task_data['thirdCard']['card']
            task.card_three_isflipped = task_data['thirdCard']['isFlipped']
            task.card_four = task_data['fourthCard']['card']
            task.card_four_isflipped = task_data['fourthCard']['isFlipped']
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