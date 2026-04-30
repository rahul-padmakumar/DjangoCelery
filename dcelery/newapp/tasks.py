from celery import shared_task

@shared_task
def mul():
    """Sample function"""
    return 3*2

@shared_task
def div():
    """Sample div fucntion"""
    return 9/3

@shared_task
def sub():
    """Sample sub function"""
    return 4-3