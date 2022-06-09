from time import sleep
from celery import shared_task
@shared_task
def prnt(req):
    sleep(5)
    print("HALO")
    print(req)
    return