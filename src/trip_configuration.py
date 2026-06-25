from src.vehicle_profile import VehicleProfile
from src.route_profile import RouteProfile
from src.weather_profile import WeatherProfile

class TripConfiguration:

    def __init__(self):
        # Typnotation. Heißt die Variable darf den Typ VehicleProfile oder None haben, wird aber hier als None initialisiert
        self.vehicle: VehicleProfile | None = None
        self.route: RouteProfile | None = None
        self.weather: WeatherProfile | None = None
        self.capacity_percent = None

    def select_vehicle(self, vehicles, selected_vehicle_number):
        if not vehicles:
            raise ValueError("Keine Fahrzeuge verfügbar.")

        if selected_vehicle_number < 1 or selected_vehicle_number > len(vehicles):
            raise ValueError("Ungültige Fahrzeugauswahl.")

        self.vehicle = vehicles[selected_vehicle_number - 1]

    def select_weather(self, weathers, selected_weather_number):
        if not weathers:
            raise ValueError("Keine Wetterdaten verfügbar.")

        if selected_weather_number < 1 or selected_weather_number > len(weathers):
            raise ValueError("Ungültige Wetterauswahl.")

        self.weather = weathers[selected_weather_number - 1]

    def select_route(self, routes, selected_route_number):
        if not routes:
            raise ValueError("Keine Routendaten verfügbar.")

        if selected_route_number < 1 or selected_route_number > len(routes):
            raise ValueError("Ungültige Routenauswahl.")

        self.route = routes[selected_route_number - 1]

    def set_capacity_percent(self, capacity_percent):
        if capacity_percent < 0 or capacity_percent > 100:
            raise ValueError("Der Batteriestand muss zwischen 0 und 100 liegen.")

        self.capacity_percent = capacity_percent