# the_drone

CELERY:
 - Terminal 1: 
   - celery -A the_drone beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
 
 - Terminal 2:
   - celery -A the_drone worker -P solo --loglevel=info