import json
import os  # os is needed for os.path.join to handle paths platform-independently.

from src.weather_profile import WeatherProfile
from src.vehicle_profile import VehicleProfile
from src.route_profile import RouteProfile, Segment

class DataLoader:
    @staticmethod
    # Using @staticmethod decorator. This allows accessing the function without instantiating a DataLoader object, e.g., DataLoader.load_weather_profiles().
    def load_weather_profiles():
        try:
            file_path = os.path.join(os.path.dirname(__file__), "weatherprofile.json")
            # __file__ is a Python variable that returns the path of the currently executed Python file.
            # os.path.dirname() returns the directory and removes the filename from the path.
            # os.path.join() combines the directory with the filename.
            with open(file_path, "r", encoding="utf-8") as data_weather:
                data = json.load(data_weather)

            weather_profiles = []
            # This list will store all created WeatherProfile objects.

            for entry in data["weatherprofiles"]:
                # data["weatherprofiles"] accesses the list of all weather entries from the JSON file.
                # The loop iterates through each entry.
                weather = WeatherProfile(
                    entry["name"],
                    entry["temperature_c"],
                    entry["rain_mm_per_h"],
                    entry["wind_speed_kmh"],
                    entry["humidity_percent"],
                    entry["weather_condition"]
                )
                # A WeatherProfile object is created from the values of the current JSON entry.

                weather_profiles.append(weather)
                # The newly created WeatherProfile object is added to the list.

            return weather_profiles
        # Returns a complete list of all WeatherProfile objects, very practical for accessing them.
        
        except FileNotFoundError:
            print("Error: The specified file 'weatherprofile.json' was not found.")
            return None
        except PermissionError:
            print("Error: Permission denied to read the file 'weatherprofile.json'.")
            return None
        except json.JSONDecodeError:
            print("Error: The file 'weatherprofile.json' contains invalid JSON.")
            return None
        except IOError as e:
            print(f"I/O error while loading 'weatherprofile.json': {e}")
            return None

    @staticmethod
    def load_vehicle_profiles():
        try:
            file_path = os.path.join(os.path.dirname(__file__), "vehicleprofile.json")
            with open(file_path, "r", encoding="utf-8") as data_vehicle:
                data = json.load(data_vehicle)

            vehicles = []

            for entry in data["vehicleprofiles"]:
                current_vehicle = VehicleProfile(
                    entry["name"],
                    entry["battery_capacity_kwh"],
                    entry["average_consumption_wh_km"],
                    entry["range_km"],
                    entry["weight_kg"]
                )
                vehicles.append(current_vehicle)

            return vehicles

        except FileNotFoundError:
            print("Error: The specified file 'vehicleprofile.json' was not found.")
            return None
        except PermissionError:
            print("Error: Permission denied to read the file 'vehicleprofile.json'.")
            return None
        except json.JSONDecodeError:
            print("Error: The file 'vehicleprofile.json' contains invalid JSON.")
            return None
        except IOError as e:
            print(f"I/O error while loading 'vehicleprofile.json': {e}")
            return None

    @staticmethod
    def load_route_profiles():
        try:
            file_path = os.path.join(os.path.dirname(__file__), "routeprofile.json")
            with open(file_path, "r", encoding="utf-8") as data_route:
                data = json.load(data_route)

            route_profiles = []

            for route_data in data["routeprofiles"]:

                segments_list = []
                for segment_input in route_data["segments"]:

                    segment = Segment(
                        segment_input["type"],
                        segment_input["distance_km"],
                        segment_input["average_speed_kmh"]
                    )
                    segments_list.append(segment)
                    # Since segments are a nested list within the JSON, they are appended directly. Thus, each route object has its own list of segments.

                route = RouteProfile(
                    route_data["name"],
                    route_data["start"],
                    route_data["destination"],
                    route_data["distance_km"],
                    route_data["altitude_ascent"],
                    route_data["altitude_descent"],
                    segments_list
                )
                
                route_profiles.append(route)

            return route_profiles
        
        except FileNotFoundError:
            print("Error: The specified file 'routeprofile.json' was not found.")
            return None
        except PermissionError:
            print("Error: Permission denied to read the file 'routeprofile.json'.")
            return None
        except json.JSONDecodeError:
            print("Error: The file 'routeprofile.json' contains invalid JSON.")
            return None
        except IOError as e:
            print(f"I/O error while loading 'routeprofile.json': {e}")
            return None