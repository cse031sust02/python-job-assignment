import json

from celery.result import AsyncResult
from django.http import HttpResponse
from django.shortcuts import render

from .tasks import my_task


def index(request):
    result = my_task.delay(100)
    return render(request, 'display_progress.html', context={'task_id': result.task_id})


def get_progress(request, task_id):
    result = AsyncResult(task_id)
    response_data = {
        'state': result.state,
        'details': result.info,
    }
    return HttpResponse(json.dumps(response_data), content_type='application/json')
