import json
import os  # os wird für os.path.join benötigt, um Pfade plattformunabhängig zu handhaben.


def load_weather_profiles():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "weatherprofile.json")
        with open(file_path, "r", encoding="utf-8") as daten_wetter:
            return json.load(daten_wetter)
    except FileNotFoundError:
        print(
            "Fehler: Die angegebene Datei 'weatherprofile.json' wurde nicht gefunden."
        )
        return None
    except PermissionError:
        print(
            "Fehler: Keine Berechtigung, um die Datei 'weatherprofile.json' zu lesen."
        )
        return None
    except json.JSONDecodeError:
        print("Fehler: Die Datei 'weatherprofile.json' enthält ungültiges JSON.")
        return None
    except IOError as e:
        print(f"Ein-/Ausgabe-Fehler beim Laden von 'weatherprofile.json': {e}")
        return None


def load_vehicle_profiles():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "vehicleprofile.json")
        with open(file_path, "r", encoding="utf-8") as daten_fahrzeug:
            return json.load(daten_fahrzeug)
    except FileNotFoundError:
        print(
            "Fehler: Die angegebene Datei 'vehicleprofile.json' wurde nicht gefunden."
        )
        return None
    except PermissionError:
        print(
            "Fehler: Keine Berechtigung, um die Datei 'vehicleprofile.json' zu lesen."
        )
        return None
    except json.JSONDecodeError:
        print("Fehler: Die Datei 'vehicleprofile.json' enthält ungültiges JSON.")
        return None
    except IOError as e:
        print(f"Ein-/Ausgabe-Fehler beim Laden von 'vehicleprofile.json': {e}")
        return None


def load_route_profiles():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "routeprofile.json")
        with open(file_path, "r", encoding="utf-8") as daten_strecke:
            return json.load(daten_strecke)
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


# Funktion zum laden einer JSON-Datei, mit Rückgabe eines spezifischen Attributs aus allen Profilen
def load_json_attributes(choose_file: str, choose_attribute: str):
    data = None
    profile_key = ""

    # Auswahl der Datei und des entsprechenden Laders
    if choose_file == "vehicleprofile":
        data = load_vehicle_profiles()
        profile_key = "fahrzeugprofile"
        print(
            f"\n--- Ausgabe des Attributs '{choose_attribute}' aus Fahrzeugprofilen ---"
        )
    elif choose_file == "routeprofile":
        data = load_route_profiles()
        profile_key = "streckenprofile"
        print(
            f"\n--- Ausgabe des Attributs '{choose_attribute}' aus Streckenprofilen ---"
        )
    elif choose_file == "weatherprofile":
        data = load_weather_profiles()
        profile_key = "wetterprofile"
        print(
            f"\n--- Ausgabe des Attributs '{choose_attribute}' aus Wetterprofilen ---"
        )
    else:
        print(
            f"Fehler: Die Datei '{choose_file}.json' ist unbekannt oder wird nicht unterstützt."
        )
        return

    # Überprüfung, ob Daten erfolgreich geladen wurden TODO Überprüfung ist eine Ergänzung von KI -> in AI.md übernehmen
    if data is None:
        print(
            f"Konnte Daten für '{choose_file}.json' nicht laden. Bitte überprüfe die Datei und die Ladefunktion."
        )
        return

    # Überprüfung, ob der erwartete Schlüssel für die Profile vorhanden ist TODO Überprüfung ist eine Ergänzung von KI -> in AI.md übernehmen
    if profile_key not in data or not isinstance(data[profile_key], list):
        print(
            f"Fehler: Der Schlüssel '{profile_key}' wurde in '{choose_file}.json' nicht gefunden oder ist keine Liste von Profilen."
        )
        return

    # Ausgabe der gewählten Attribute
    found_any_attribute = False
    for i, profile in enumerate(data[profile_key]):
        attribute_value = profile.get(choose_attribute)
        if attribute_value is not None:
            print(f"  Profil {i+1}: {choose_attribute} = {attribute_value}")
            found_any_attribute = True
        else:
            print(f"  Profil {i+1}: Attribut '{choose_attribute}' nicht gefunden.")

    if not found_any_attribute:
        print(f"Keines der Profile enthielt das Attribut '{choose_attribute}'.")
