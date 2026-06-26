from src.data_loader import DataLoader
from src.console_ui import ConsoleUI


def main():
    print("===========================================")
    print("Weather-aware EV Range Assistant started")
    print("===========================================\n\n")

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