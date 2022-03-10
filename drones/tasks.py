from the_drone.celery import app


@app.task()
def checking_battery_level():
    """

    :return:
    """
    from drones.models import Drone, HistoryBatteryLevel

    for drone in Drone.objects.all():
        HistoryBatteryLevel.objects.create(
            drone=drone,
            battery=drone.battery_capacity
        )
