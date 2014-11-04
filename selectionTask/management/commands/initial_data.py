import django
from django.core.management import BaseCommand
from django.db import transaction


@transaction.atomic
def create_initial_data():
    pass


class Command(BaseCommand):
    args = ''
    help = 'Creates initial task data in the database'

    def handle(self, *args, **options):
        self.stdout.write("Creating initial task data ...\n")
        create_initial_data()