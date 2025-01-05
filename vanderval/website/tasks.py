import json
import logging
import redis

from time import sleep

from .models import Site, UserRecords

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)

def task_01(site_id: int):
    TIME_MULTIPLIER = 0.001 # very fast execution per record
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 01: {} processed".format(record.name))
    return True


def task_02(site_id: int):
    TIME_MULTIPLIER = 0.01
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 02: {} processed".format(record.name))
    return True


def task_03(site_id: int):
    TIME_MULTIPLIER = 0.1
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 03: {} processed".format(record.name))
    return True


def task_04(site_id: int):
    TIME_MULTIPLIER = 1
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 04: {} processed".format(record.name))
    return True


def task_05(site_id: int):
    TIME_MULTIPLIER = 10
    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site)
    for record in records:
        sleep(TIME_MULTIPLIER)
        logger.info("Task 05: {} processed".format(record.name))
    return True

# To execute the tasks
def task_executor(site_id, job_type):
    task_map = {
        "task_01": 0.001,
        "task_02": 0.01,
        "task_03": 0.1,
        "task_04": 1,
        "task_05": 10,
    }

    site = Site.objects.get(id=site_id)
    records = UserRecords.objects.filter(site=site, is_active=True)

    for record in records:
        sleep(task_map[job_type])
        print(f"{job_type}: Processed {record.name}")
    return True

# Worker is responsible to start task executer
def worker_function():
    print("Worker started")
    while True:
        job = redis_conn.lpop('job_queue')
        if job:
            job_data = json.loads(job)
            site_id = job_data['site_id']
            job_type = job_data['job_type']
            try:
                task_executor(site_id, job_type)
            except Exception as e:
                print("Error processing Job", e)
                logger.error(f"Error processing job {job_data}: {str(e)}")
        sleep(1)
