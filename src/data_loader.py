import json
import os  # os wird für os.path.join benötigt, um Pfade plattformunabhängig zu handhaben.

from src.weather_profile import WeatherProfile
from src.vehicle_profile import VehicleProfile
from src.route_profile import RouteProfile, Segment


class DataLoader:
    @staticmethod
    # Verzicht auf self-Teil der Funktion. Damit muss kein Objekt erzeugt werden von der Klasse DataLoader, um auf die Funktionen zuzugreifen. Zugriff jetzt mit DataLoader.load_weather_profiles()
    def load_weather_profiles():
        try:
            file_path = os.path.join(os.path.dirname(__file__), "weatherprofile.json")
            # __file__ ist eine Python-Variable und gibt den Pfad der aktuell ausgeführten Python-Datei zurück.
            # os.path.dirname() gibt das Verzeichnis zurück und entfernt den Dateinamen aus dem Pfad
            # os.path.join() fügt die zweite Variable in das Verzeichnis ein
            with open(file_path, "r", encoding="utf-8") as data_weather:
                data = json.load(data_weather)


            weather_situation = []
            # In dieser Liste werden später alle erzeugten WeatherProfile-Objekte gespeichert.

            for entry in data["weatherprofiles"]:
                # data["weatherprofiles"] greift auf die Liste mit allen Wettereinträgen aus der JSON-Datei zu.
                # Die Schleife geht jeden einzelnen Eintrag nacheinander durch.
                weather = WeatherProfile(
                    entry["name"],
                    entry["temperature_c"],
                    entry["rain_mm_per_h"],
                    entry["wind_speed_kmh"],
                    entry["humidity_percent"],
                    entry["weather_condition"]
                )
                 # Aus den Werten des aktuellen JSON-Eintrags wird ein WeatherProfile-Objekt erzeugt.

                weather_situation.append(weather)
                # Das neu erzeugte WeatherProfile-Objekt wird zur Liste hinzugefügt.

            return weather_situation
        # Rückgabe einer kompletten Liste mit allen WeatherProfile-Objekten. Sehr praktisch für den Zugriff auf die Objekte
        
        except FileNotFoundError:
            print("Fehler: Die angegebene Datei 'weatherprofile.json' wurde nicht gefunden.")
            return None
        except PermissionError:
            print("Fehler: Keine Berechtigung, um die Datei 'weatherprofile.json' zu lesen.")
            return None
        except json.JSONDecodeError:
            print("Fehler: Die Datei 'weatherprofile.json' enthält ungültiges JSON.")
            return None
        except IOError as e:
            print(f"Ein-/Ausgabe-Fehler beim Laden von 'weatherprofile.json': {e}")
            return None

    @staticmethod
    def load_vehicle_profiles():
        try:
            file_path = os.path.join(os.path.dirname(__file__), "vehicleprofile.json")
            with open(file_path, "r", encoding="utf-8") as data_vehicles:
                data = json.load(data_vehicles)

            vehicles = []

            for entry in data["vehicleprofiles"]:
                vehicle = VehicleProfile(
                    entry["name"],
                    entry["capacity_kwh"],
                    entry["average_consumption_wh_km"],
                    entry["range_km"],
                    entry["weight_kg"]
                )
                vehicles.append(vehicle)

            return vehicles

        except FileNotFoundError:
            print("Fehler: Die angegebene Datei 'vehicleprofile.json' wurde nicht gefunden.")
            return None
        except PermissionError:
            print("Fehler: Keine Berechtigung, um die Datei 'vehicleprofile.json' zu lesen.")
            return None
        except json.JSONDecodeError:
            print("Fehler: Die Datei 'vehicleprofile.json' enthält ungültiges JSON.")
            return None
        except IOError as e:
            print(f"Ein-/Ausgabe-Fehler beim Laden von 'vehicleprofile.json': {e}")
            return None

    @staticmethod
    def load_route_profiles():
        try:
            file_path = os.path.join(os.path.dirname(__file__), "routeprofile.json")
            with open(file_path, "r", encoding="utf-8") as data_strecke:
                data = json.load(data_strecke)

            routeprofiles = []

            for entry in data["routeprofiles"]:

                segments_list = []
                for segment_entry in entry["segments"]:

                    segment = Segment(
                    segment_entry["type"],
                    segment_entry["distance_km"],
                    segment_entry["average_speed_kmh"]
                )
                    segments_list.append(segment)
                    # Da Segmente in der JSON eine eigene kleine Liste sind, habe ich das einfach mit angehängt. Somit hat jedes Objekt eine Segmente-Liste

                route = RouteProfile(
                entry["name"],
                entry["start"],
                entry["destination"],
                entry["distance_km"],
                entry["altitude_ascent"],
                entry["altitude_descent"],
                segments_list
            )
                
                routeprofiles.append(route)

            return routeprofiles
        

        except FileNotFoundError:
            print("Fehler: Die angegebene Datei 'routeprofile.json' wurde nicht gefunden.")
            return None
        except PermissionError:
            print("Fehler: Keine Berechtigung, um die Datei 'routeprofile.json' zu lesen.")
            return None
        except json.JSONDecodeError:
            print("Fehler: Die Datei 'routeprofile.json' enthält ungültiges JSON.")
            return None
        except IOError as e:
            print(f"Ein-/Ausgabe-Fehler beim Laden von 'routeprofile.json': {e}")
            return None