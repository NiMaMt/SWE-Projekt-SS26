import json


def load_weather_profiles():
    try:
        with open("src/weatherprofile.json", "r", encoding="utf-8") as daten_wetter:
            return json.load(daten_wetter)
    except FileNotFoundError:
        print("Fehler: Die angegebene Datei wurde nicht gefunden")
    except PermissionError:
        print("Fehler: Keine Berechtigung, um diese Datei zu lesen.")
    except IOError as e:
        print(f"Ein-/Ausgabe-Fehler: {e}")


def load_vehicle_profiles():
    try:
        with open("src/vehicleprofile.json", "r", encoding="utf-8") as daten_fahrzeug:
            return json.load(daten_fahrzeug)
    except FileNotFoundError:
        print("Fehler: Die angegebene Datei wurde nicht gefunden")
    except PermissionError:
        print("Fehler: Keine Berechtigung, um diese Datei zu lesen.")
    except IOError as e:
        print(f"Ein-/Ausgabe-Fehler: {e}")


def load_route_profiles():
    try:
        with open("src/routeprofile.json", "r", encoding="utf-8") as daten_strecke:
            return json.load(daten_strecke)
    except FileNotFoundError:
        print("Fehler: Die angegebene Datei wurde nicht gefunden")
    except PermissionError:
        print("Fehler: Keine Berechtigung, um diese Datei zu lesen.")
    except IOError as e:
        print(f"Ein-/Ausgabe-Fehler: {e}")


# Funktion zum Ausgeben der Namen aus weatherprofile.json
def print_weather_profile():
    data = load_weather_profiles()

    # In der print() Funktion "name ersetzen für das Attribut, was ausgegeben werden soll"
    for profil in data["wetterprofile"]:
        print(profil["name"])


# Funktion zum Ausgeben der Namen aus vehicleprofile.json
def print_vehicle_profile():
    data = load_vehicle_profiles()

    for profil in data["fahrzeugprofile"]:
        print(profil["name"])


# Funktion zum Ausgeben der Namen aus routeprofile.json
def print_route_profile():
    data = load_route_profiles()

    for profil in data["streckenprofile"]:
        print(profil["name"])
