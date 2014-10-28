from django.shortcuts import render
from django.http import HttpResponse
from models import Subject, AbstractTask, ConcreteTask, Task, Result
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
        'task_id': task.pk,
        'description': task.description,
        1: {
            'card_id': task.card_one
        },
        2: {
            'card_id': task.card_two
        },
        3: {
            'card_id': task.card_three
        },
        4: {
            'card_id': task.card_four
        },
        'story': task.story,
        'task_number': min(AbstractTask.objects.count(), ConcreteTask.objects.count()),
        'progress': subject.results.count()
    }), content_type='application/json')


@csrf_exempt
def submit(request):
    if not 'id' in request.POST:
        return HttpResponse('{"Error": "No ID supplied."}', content_type='application/json', status=400)
    if not 'result_data' in request.POST:
        return HttpResponse('{"Error": "No result data supplied."}', content_type='application/json', status=400)
    try:
        subject = Subject.objects.filter(subject_id=request.POST['id']).all()[0]
    except IndexError:
        return HttpResponse('{"Error": "Unknown id."}', content_type='application/json')
    result_data = json.loads(request.POST['result_data'])
    try:
        task = Task.objects.filter(pk=result_data['task_id']).all()[0]
    except IndexError:
        return HttpResponse('{"Error": "Unknown task."}', content_type='application/json')
    result = Result(subject=subject, task=task)
    result.card_one_isflipped = result_data['1']
    result.card_two_isflipped = result_data['2']
    result.card_three_isflipped = result_data['3']
    result.card_four_isflipped = result_data['4']
    result.save()
    if subject.results.count() >= min(AbstractTask.objects.count(), ConcreteTask.objects.count()):
        return HttpResponse('{"Finished": "Tasks completed."}', content_type='application/json')
    if subject.is_abstract_group():
        task = AbstractTask.objects.all()[subject.results.count()]
    else:
        task = ConcreteTask.objects.all()[subject.results.count()]
    return HttpResponse(json.dumps({
        'task_id': task.pk,
        'description': task.description,
        1: {
            'card_id': task.card_one
        },
        2: {
            'card_id': task.card_two
        },
        3: {
            'card_id': task.card_three
        },
        4: {
            'card_id': task.card_four
        },
        'story': task.story,
        'task_number': min(AbstractTask.objects.count(), ConcreteTask.objects.count()),
        'progress': subject.results.count()
    }), content_type='application/json')


def assign_task_type():
    return randrange(0, 2) == 1