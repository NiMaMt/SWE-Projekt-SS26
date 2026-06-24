import pytest

from src.trip_configuration import TripConfiguration
from src.vehicle_profile import VehicleProfile
from src.route_profile import RouteProfile
from src.weather_profile import WeatherProfile
from src.data_loader import DataLoader

# Vergleicht ob fiktiv der zweite Eintrag gewählt wurde von vehicleprofile.json
def test_select_vehicle_valid():
    trip_config = TripConfiguration()
    vehicles = DataLoader.load_vehicle_profiles()

    trip_config.select_vehicle(vehicles, 2)

    assert trip_config.vehicle == vehicles[1]
    assert isinstance(trip_config.vehicle, VehicleProfile)
    assert trip_config.vehicle.name == "Volkswagen ID.Polo"
    assert trip_config.vehicle.capacity_kwh == 51.7
    assert trip_config.vehicle.average_consumption_wh_km == 154.0
    assert trip_config.vehicle.range_km == 335.0
    assert trip_config.vehicle.weight_kg == 1576.0

# Haut eine leere Liste in das Objekt von TripConfiguration
def test_select_vehicle_empty_list():
    trip_config = TripConfiguration()
    vehicles = []

    with pytest.raises(ValueError, match="Keine Fahrzeuge verfügbar."):
        trip_config.select_vehicle(vehicles, 1)

# Falls die Eingabe ungültig war
def test_select_vehicle_invalid_selection():
    trip_config = TripConfiguration()
    vehicles = DataLoader.load_vehicle_profiles()

    with pytest.raises(ValueError, match="Ungültige Fahrzeugauswahl."):
        trip_config.select_vehicle(vehicles, 0)

def test_select_weather_valid():
    trip_config = TripConfiguration()
    weathers = DataLoader.load_weather_profiles()

    trip_config.select_weather(weathers, 1)

    assert trip_config.weatherprofile == weathers[0]
    assert isinstance(trip_config.weatherprofile, WeatherProfile)
    assert trip_config.weatherprofile.name == "Sonniger Sommertag"
    assert trip_config.weatherprofile.temperature_c == 28
    assert trip_config.weatherprofile.rain_mm_per_h == 0
    assert trip_config.weatherprofile.wind_speed_kmh == 12
    assert trip_config.weatherprofile.humidity_percent == 45
    assert trip_config.weatherprofile.weather_condition == "sonnig"

def test_select_route_valid():
    trip_config = TripConfiguration()
    routes = DataLoader.load_route_profiles()

    trip_config.select_route(routes, 1)

    assert trip_config.route == routes[0]
    assert isinstance(trip_config.route, RouteProfile)
    assert trip_config.route.name == "Esslingen am Neckar -> Stuttgart"
    assert trip_config.route.start == "Esslingen am Neckar"
    assert trip_config.route.destination == "Stuttgart"
    assert trip_config.route.distance_km == 17
    assert trip_config.route.altitude_ascent == 120
    assert trip_config.route.altitude_descent == 95
    assert trip_config.route.segments[0].type == "Stadt"
    assert trip_config.route.segments[0].distance_km == 8
    assert trip_config.route.segments[0].average_speed_kmh == 35

def test_set_capacity_percent_valid():
    trip_config = TripConfiguration()

    trip_config.set_capacity_percent(50)

    assert trip_config.capacity_percent == 50
    assert isinstance(trip_config.capacity_percent, int)

def test_set_capacity_percent_below_zero():
    trip_config = TripConfiguration()

    with pytest.raises(ValueError, match="Der Batteriestand muss zwischen 0 und 100 liegen."):
        trip_config.set_capacity_percent(-1)

def test_set_capacity_percent_above_hundred():
    trip_config = TripConfiguration()

    with pytest.raises(ValueError, match="Der Batteriestand muss zwischen 0 und 100 liegen."):
        trip_config.set_capacity_percent(101)

def test_set_capacity_percent_boundary_values():
    trip_config = TripConfiguration()

    trip_config.set_capacity_percent(0)
    assert trip_config.capacity_percent == 0.0 or trip_config.capacity_percent == 0

    trip_config.set_capacity_percent(100)
    assert trip_config.capacity_percent == 100.0 or trip_config.capacity_percent == 100