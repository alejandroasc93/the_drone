from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'the_drone.settings')
app = Celery('the_drone')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'checking-battery-level': {
        'task': 'drones.tasks.checking_battery_level',
        'schedule': crontab(minute='*/10'),
        'args': (),
    },
}
