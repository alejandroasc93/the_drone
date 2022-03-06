from drones.views import create_drone_view
from the_drone.urls import routers

routers.register(r'drone/create', create_drone_view, basename='create_drone_view')

urlpatterns = []
