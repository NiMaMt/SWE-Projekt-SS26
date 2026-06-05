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
            with open(file_path, "r", encoding="utf-8") as daten_wetter:
                daten = json.load(daten_wetter)


            wettersituation = []
            # In dieser Liste werden später alle erzeugten WeatherProfile-Objekte gespeichert.

            for eintrag in daten["wetterprofile"]:
                # daten["wetterprofile"] greift auf die Liste mit allen Wettereinträgen aus der JSON-Datei zu.
                # Die Schleife geht jeden einzelnen Eintrag nacheinander durch.
                wetter = WeatherProfile(
                    eintrag["name"],
                    eintrag["temperatur_c"],
                    eintrag["regen_mm_pro_h"],
                    eintrag["windgeschwindigkeit_kmh"],
                    eintrag["luftfeuchtigkeit_prozent"],
                    eintrag["wetterzustand"]
                )
                 # Aus den Werten des aktuellen JSON-Eintrags wird ein WeatherProfile-Objekt erzeugt.

                wettersituation.append(wetter)
                # Das neu erzeugte WeatherProfile-Objekt wird zur Liste hinzugefügt.

            return wettersituation
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
            with open(file_path, "r", encoding="utf-8") as daten_fahrzeug:
                daten = json.load(daten_fahrzeug)

            fahrzeuge = []

            for eintrag in daten["fahrzeugprofile"]:
                fahrzeug = VehicleProfile(
                    eintrag["name"],
                    eintrag["batteriekapazitaet_kwh"],
                    eintrag["durchschnittlicher_basisverbrauch_wh_km"],
                    eintrag["reichweite_km"],
                    eintrag["gewicht_kg"]
                )
                fahrzeuge.append(fahrzeug)

            return fahrzeuge

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
            with open(file_path, "r", encoding="utf-8") as daten_strecke:
                daten = json.load(daten_strecke)

            streckenprofile = []

            for eintrag in daten["streckenprofile"]:

                segmente_liste = []
                for segment_eintrag in eintrag["segmente"]:

                    segment = Segment(
                    segment_eintrag["typ"],
                    segment_eintrag["distanz_km"],
                    segment_eintrag["durchschnittsgeschwindigkeit_kmh"]
                )
                    segmente_liste.append(segment)
                    # Da Segmente in der JSON eine eigene kleine Liste sind, habe ich das einfach mit angehängt. Somit hat jedes Objekt eine Segmente-Liste

                route = RouteProfile(
                eintrag["name"],
                eintrag["start"],
                eintrag["ziel"],
                eintrag["gesamtdistanz_km"],
                eintrag["hoehenmeter_bergauf"],
                eintrag["hoehenmeter_bergab"],
                segmente_liste
            )
                
                streckenprofile.append(route)

            return streckenprofile
        

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