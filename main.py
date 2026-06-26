from src.data_loader import DataLoader
from src.console_ui import ConsoleUI
from src.trip_configuration import TripConfiguration
from src.rangeService import RangeService

#-------------------------------------------------------------------------------
#Hilfsmethoden
#-------------------------------------------------------------------------------

def controll_user_input_integer(prompt, min_value=None, max_value=None):
    
    # Kontrolliert die Benutzereingabe von Integer Werten mit Wiederholung der Eingabeaufforderung bei ungültiger Eingabe.

    while True:
        try:
            value = int(input(prompt + ": "))
            
            # Bereichsprüfung
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Ihre Eingabe liegt nicht im Auswahlbereich. Versuchen Sie es erneut.")
                continue
                                
            return value
            
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")

def controll_user_input_float(prompt, min_value=None, max_value=None):
    
    # Kontrolliert die Benutzereingabe von Float Werten mit Wiederholung der Eingabeaufforderung bei ungültiger Eingabe.

    while True:
        try:
            value = float(input(prompt + ": "))
            
            # Bereichsprüfung
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Ihre Eingabe liegt nicht im Auswahlbereich. Versuchen Sie es erneut.")
                continue
                                
            return value
            
        except ValueError:
            print("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")


def get_valid_string_choice(prompt, option1, option2):

    option1_upper = option1.upper()
    option2_upper = option2.upper()

    while True:
        try:
            user_input = input(prompt + ": ").strip().upper()
                        
            if user_input == option1_upper or user_input == option2_upper:
                return user_input
            else:
                print(f"Bitte geben Sie '{option1}' oder '{option2}' ein.")     

        except KeyboardInterrupt:
            print(f"Bitte geben Sie '{option1}' oder '{option2}' ein.")
            return None


#-------------------------------------------------------------------------------
#Main Methode
#-------------------------------------------------------------------------------


def main():
    print("===========================================")
    print("Weather-aware EV Range Assistant started")
    print("===========================================\n\n")


    try:
        #-----Daten laden-----
        #Fahrzeugdaten laden
        print("Lade Fahrzeugdaten...")
        vehicles = DataLoader.load_vehicle_profiles()
        if not vehicles:
            print("Fehler: Keine Fahrzeuge verfügbar.")
            return False
        
        #Wetterdaten laden 
        print("Lade Wetterdaten...")
        weathers = DataLoader.load_weather_profiles()
        if not weathers:
            print("Fehler: Keine Wetterdaten verfügbar.")
            return False
            
        #Routendaten laden 
        print("Lade Routendaten...")
        routes = DataLoader.load_route_profiles()
        if not routes:
            print("Fehler: Keine Routen verfügbar.")
            return False
            
        print("Alle Daten erfolgreich geladen.\n")
        
        #-----TripConfiguration Objekt erstellen-----
        trip_config = TripConfiguration()

        #-----Benutzereingaben-----
        #Fahrzeug auswählen
        print("=== Fahrzeugauswahl ===")
        ConsoleUI.print_vehicle(vehicles)
        print()

        selected_vehicle_number = controll_user_input_integer("Wählen Sie ein Fahrzeug durch Eingabe der entsprechenden Nummer", 1, len(vehicles))
        trip_config.select_vehicle(vehicles, selected_vehicle_number)
        print(f"Gewähltes Fahrzeug: {trip_config.vehicle.name}\n")
        
        #Wetter auswählen
        print("=== Wetterauswahl ===")
        ConsoleUI.print_weather(weathers)
        print()
        
        selected_weather_number = controll_user_input_integer("Wählen Sie ein Wetter durch Eingabe der entsprechenden Nummer", 1, len(weathers))
        trip_config.select_weather(weathers, selected_weather_number)
        print(f"Gewähltes Wetter: {trip_config.weather.name}\n")
        
        #Route auswählen
        print("=== Routenauswahl ===")
        ConsoleUI.print_route(routes)
        print()
        
        selected_route_number = controll_user_input_integer("Wählen Sie eine Route durch Eingabe der entsprechenden Nummer", 1, len(routes))
        trip_config.select_route(routes, selected_route_number)
        print(f"Gewählte Route: {trip_config.route.name}\n")
        
        #Batteriestand eingeben
        print("=== Batteriestand ===")
        capacity_percent = controll_user_input_float("Geben Sie den aktuellen Batteriestand in Prozent ein", 0,100)
        trip_config.set_capacity_percent(capacity_percent)
        print(f"Eingegebener Batteriestand: {capacity_percent}%\n")
        
        #Überblick Anzeigen
        print("=== Konfiguration abgeschlossen ===")
        ConsoleUI.print_selected_configuration(trip_config)
        
        
        #-----Berechnung-----
        print("=== Routenberechnung ===")
        print("Ihre Route wird berechnet...")

        trip_possibility = RangeService.check_drive_possible(trip_config)

        if trip_possibility.trip_possible:
            print("Die Fahrt ist mit Ihrem aktuellen Batteriestand möglich")
            print(f"Erwartete Restkapazität am Ziel: {trip_possibility.residual_capacity_kwh:.2f} kWh")
        else:
            print("!ACHTUNG! Das Erreichen des Ziels ist mit Ihrem aktuellen Batteriestand NICHT möglich")
            print(f"Fehlende Kapazität: {trip_possibility.lack_capacity_kwh:.2f} kWh")
            chargeOption = get_valid_string_choice("Möchten Sie eine Ladestation auf Ihrer Route suchen? (J/N)", "J", "N")
            print(f"Diese Funktion ist mit ihrem aktuellen Abonnement leider nicht verfügbar. Bitte kontaktieren Sie ihren Service Partner für weitere Informationen.\n")




        return True

    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return False


# Späterer Ablauf:
    # vehicles kommt von DataLoader
    # selected_vehicle_number = int(input("Wählen Sie ein Fahrzeug: "))
    # TripConfiguration.select_vehicle(vehicles, selected_vehicle_number)
    #
    # selected_weather_number = int(input("Wählen Sie eine Wettersituation: "))
    # TripConfiguration.select_weather(weathers, selected_weather_number)
    #
    # selected_route_number = int(input("Wählen Sie eine Route: "))
    # TripConfiguration.select_route(routes, selected_route_number)
    #
    # capacity_percent = float(input("Geben Sie den aktuellen Batteriestand in Prozent ein: "))
    # TripConfiguration.set_capacity_percent(capacity_percent)
 
    # 1. Objekte erzeugen mit DataLoader, quasi vehicles = load_vehicle_profiles()
    # 2. Objekte übergeben an ConsoleUI an die print_vehicles(vehicles)
    # 3. Objekt wählen mit TripConfiguration:
    #       selected_vehicle_number = int(input("Wählen Sie ein Fahrzeug: "))
    #       TripConfiguration.select_vehicle(vehicles, selected_vehicle_number)
    # 4. Objekt vom Typ TripConfiguration erstellen mit den Werten aus den Eingaben. Da gibts bestimmt ne Anleitung wie das geht
    # 5. RangeService Funktionen nutzen mit übergabe des TripConfiguration Objektes, rangeService.calculate_energy_available(TripConfiguration-Objekt)

    
if __name__ == "__main__":
    main()