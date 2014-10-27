from django.shortcuts import render
from django.http import HttpResponse
from models import Subject, AbstractTask, ConcreteTask
from random import randrange
from django.views.decorators.csrf import csrf_exempt
import os
import json


def home(request):
    with open(os.path.join(os.path.dirname(__file__), "../static/index.html"), 'r') as index_html_file:
        return HttpResponse(index_html_file.read(), content_type='text/html')


@csrf_exempt
def assign(request):
    if not 'id' in request.POST:
        return HttpResponse('{"Error": "No ID supplied."}', content_type='application/json', status=400)
    try:
        subject = Subject.objects.filter(subject_id=request.POST['id']).all()[0]
    except IndexError:
        subject = Subject(subject_id=request.POST['id'], group=assign_task_type())
        subject.save()
    if subject.results.count() >= min(AbstractTask.objects.count(), ConcreteTask.objects.count()):
        return HttpResponse('{"Error": "Tasks already completed. If you came you came to this from the pre-treatment, '
                            'please contact your survey company"}', content_type='application/json')
    if subject.is_abstract_group():
        task = AbstractTask.objects.all()[subject.results.count()]
    else:
        task = ConcreteTask.objects.all()[subject.results.count()]
    return HttpResponse(json.dumps({
        'description': task.description,
        1: {
            'card_id': task.card_one,
            'is_flipped': task.card_one_isflipped
        },
        2: {
            'card_id': task.card_two,
            'is_flipped': task.card_two_isflipped
        },
        3: {
            'card_id': task.card_three,
            'is_flipped': task.card_three_isflipped
        },
        4: {
            'card_id': task.card_four,
            'is_flipped': task.card_four_isflipped
        }
    }), content_type='application/json')


def submit(request):
    pass


def assign_task_type():
    return randrange(0, 2) == 1