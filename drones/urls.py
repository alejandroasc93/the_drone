from drones.views import create_drone_view, create_medicines_loaded_by_drone_view, checking_loaded_medication_view
from the_drone.urls import routers

routers.register(r'drone/create', create_drone_view, basename='create_drone_view')
routers.register(r'drone/load-medication', create_medicines_loaded_by_drone_view,
                 basename='create_medicines_loaded_by_drone_view')
routers.register(r'drone', checking_loaded_medication_view,
                 basename='checking_loaded_medication_view')

urlpatterns = []
