from django.http import HttpResponse


def index(request):
    demo_progress.delay()
    return HttpResponse('demo progress done!')
