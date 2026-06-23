from src.console_ui import ConsoleUI
from src.weather_profile import WeatherProfile
from src.route_profile import RouteProfile, Segment
from src.vehicle_profile import VehicleProfile


# Test Fahrzeug ausgewählt
def test_select_car():
    test_fahrzeug = [VehicleProfile("Tesla", 100, 20, 500, 2000) ]