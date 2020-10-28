import random
from celery import shared_task


@shared_task
def demo_progress():
    number = random.randint(1, 100)
    print(number)
    return number
