from src.data_loader import DataLoader
from src.console_ui import ConsoleUI
from src.trip_configuration import TripConfiguration
from src.rangeService import RangeService

def main():
    print("================================")
    print("Weather-aware EV Range Assistant")
    print("================================\n\n")

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
        ConsoleUI.select_vehicle(trip_config, vehicles)
        ConsoleUI.select_weather(trip_config, weathers)
        ConsoleUI.select_route(trip_config, routes)
        ConsoleUI.set_capacity_percent(trip_config)  

        #Überblick Anzeigen
        print("=== Konfiguration abgeschlossen ===")
        ConsoleUI.print_selected_configuration(trip_config)
        
        #-----Berechnung-----
        print("=== Routenberechnung ===")
        print("Ihre Route wird berechnet...")

        trip_possibility = RangeService.check_drive_possible(trip_config)

        if trip_possibility.trip_possible:
            # Umrechnung von Wh in kWh für die Ausgabe
            residual_capacity_kwh = trip_possibility.residual_capacity_wh / 1000
            print("Die Fahrt ist mit Ihrem aktuellen Batteriestand möglich")
            print(f"Erwartete Restkapazität am Ziel: {residual_capacity_kwh:.2f} kWh")
        else:
            # Umrechnung von Wh in kWh für die Ausgabe
            lack_capacity_kwh = trip_possibility.lack_capacity_wh / 1000
            print("!ACHTUNG! Das Erreichen des Ziels ist mit Ihrem aktuellen Batteriestand NICHT möglich")
            print(f"Fehlende Kapazität: {lack_capacity_kwh:.2f} kWh")
            
            ConsoleUI.get_string_choice("Möchten Sie eine Ladestation auf Ihrer Route suchen? (J/N)","J","N")
            print(f"Diese Funktion ist mit ihrem aktuellen Abonnement leider nicht verfügbar. Bitte kontaktieren Sie ihren Service Partner für weitere Informationen.\n")

        return True

    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        return False
    
    

    

    
if __name__ == "__main__":
    main()