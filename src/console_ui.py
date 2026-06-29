class ConsoleUI:
 
    @staticmethod
    def format_weather_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Name':<30}"
            f"{'Temp.':>8}"
            f"{'Regen':>12}"
            f"{'Wind':>12}"
            f"{'Luftf.':>10}"
            f"   Zustand"
        )
 
        separation_line = "-" * len(header)
        rows = [header, separation_line]
 
        for nummer, item in enumerate(data, start=1):
            rows.append(
                f"{nummer:<4}"
                f"{item.name:<30}"
                f"{item.temperature_c:>6.1f} °C"
                f"{item.rain_mm_per_h:>8.1f} mm/h"
                f"{item.wind_speed_kmh:>8.1f} km/h"
                f"{item.humidity_percent:>6.1f}%"
                f"   {item.weather_condition}"
            )
 
        return "\n".join(rows)
 
    @staticmethod
    def print_weather(data):
        print(ConsoleUI.format_weather_list(data))
 
    @staticmethod
    def format_vehicle_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Name':<38}"
            f"{'Kapazität':>12}"
            f"{'Verbrauch':>15}"
            f"{'Reichweite':>14}"
            f"{'Gewicht':>12}"
        )
 
        separation_line = "-" * len(header)
        rows = [header, separation_line]
 
        for nummer, item in enumerate(data, start=1):
            rows.append(
                f"{nummer:<4}"
                f"{item.name:<38}"
                f"{item.capacity_kwh:>8.1f} kWh"
                f"{item.average_consumption_wh_km:>10.1f} Wh/km"
                f"{item.range_km:>10.1f} km"
                f"{item.weight_kg:>10.1f} kg"
            )
 
        return "\n".join(rows)
 
    @staticmethod
    def print_vehicle(data):
        print(ConsoleUI.format_vehicle_list(data))
 
    @staticmethod
    def format_route_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Name':<35}"
            f"{'Start':<23}"
            f"{'Ziel':<23}"
            f"{'Distanz':>12}"
            f"{'+Höhenm.':>12}"
            f"{'-Höhenm.':>12}"
        )
 
        separation_line = "-" * len(header)
        rows = [header, separation_line]
 
        for nummer, item in enumerate(data, start=1):
            rows.append(
                f"{nummer:<4}"
                f"{item.name:<35}"
                f"{item.start:<23}"
                f"{item.destination:<23}"
                f"{item.distance_km:>9} km"
                f"{item.altitude_ascent:>9} m"
                f"{item.altitude_descent:>9} m"
            )
 
        return "\n".join(rows)
 
    @staticmethod
    def print_route(data):
        print(ConsoleUI.format_route_list(data))
 
    @staticmethod
    def format_segment_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Routentyp':<18}"
            f"{'Länge':<12}"
            f"{'Durchschnittsgeschw.':<15}"
        )
 
        separation_line = "-" * len(header)
        rows = [header, separation_line]
 
        for nummer, item in enumerate(data, start=1):
            rows.append(
                f"{nummer:<4}"
                f"{item.type:<18}"
                f"{f'{item.distance_km} km':<12}"
                f"{f'{item.average_speed_kmh} km/h':<15}"
            )
 
        return "\n".join(rows)
 
    @staticmethod
    def print_segment(route):
        print(ConsoleUI.format_segment_list(route.segments))
 
    @staticmethod
    def print_selected_configuration(config):
        print("=== Ihre gewählte Konfiguration ===\n")
        print(f"Fahrzeug   : {config.vehicle.name}")
        print(f"Reichweite : {config.vehicle.range_km} km\n")
        print(f"Route      : {config.route.name}")
        print(f"Distanz    : {config.route.distance_km} km\n")
        print(f"Wetter     : {config.weather.name}")
        print(f"Temperatur : {config.weather.temperature_c} °C")
        print(f"Zustand    : {config.weather.weather_condition}\n")
        print(f"Ladestatus : {config.capacity_percent} %")
 
    @staticmethod
    def get_integer_input(prompt, min_value=None, max_value=None):
        while True:
            try:
                value = int(input(prompt + ": "))
 
                if (min_value is not None and value < min_value) or (
                    max_value is not None and value > max_value
                ):
                    print("Ihre Eingabe liegt nicht im Auswahlbereich. Versuchen Sie es erneut.")
                    continue
 
                return value
 
            except ValueError:
                print("Ungültige Eingabe! Bitte geben Sie eine ganze Zahl ein.")
 
    @staticmethod
    def get_float_input(prompt, min_value=None, max_value=None):
        while True:
            try:
                value = float(input(prompt + ": "))
 
                if (min_value is not None and value < min_value) or (
                    max_value is not None and value > max_value
                ):
                    print("Ihre Eingabe liegt nicht im Auswahlbereich. Versuchen Sie es erneut.")
                    continue
 
                return value
 
            except ValueError:
                print("Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")
 
    @staticmethod
    def get_string_choice(prompt, option1, option2):
        option1_upper = option1.upper()
        option2_upper = option2.upper()
 
        while True:
            user_input = input(prompt + ": ").strip().upper()
 
            if user_input == option1_upper or user_input == option2_upper:
                return user_input
 
            print(f"Bitte geben Sie '{option1}' oder '{option2}' ein.")
 
    @staticmethod
    def select_vehicle(trip_config, vehicles):
        print("=== Fahrzeugauswahl ===")
        ConsoleUI.print_vehicle(vehicles)
        print()
 
        while True:
            try:
                selected_vehicle_number = ConsoleUI.get_integer_input(
                    "Wählen Sie ein Fahrzeug durch Eingabe der entsprechenden Nummer",
                    1,
                    len(vehicles)
                )
                trip_config.select_vehicle(vehicles, selected_vehicle_number)
                print(f"Gewähltes Fahrzeug: {trip_config.vehicle.name}\n")
                return
            except ValueError as e:
                print(f"{e} Bitte versuchen Sie es erneut.\n")
 
    @staticmethod
    def select_weather(trip_config, weathers):
        print("=== Wetterauswahl ===")
        ConsoleUI.print_weather(weathers)
        print()
 
        while True:
            try:
                selected_weather_number = ConsoleUI.get_integer_input(
                    "Wählen Sie ein Wetter durch Eingabe der entsprechenden Nummer",
                    1,
                    len(weathers)
                )
                trip_config.select_weather(weathers, selected_weather_number)
                print(f"Gewähltes Wetter: {trip_config.weather.name}\n")
                return
            except ValueError as e:
                print(f"{e} Bitte versuchen Sie es erneut.\n")
 
    @staticmethod
    def select_route(trip_config, routes):
        print("=== Routenauswahl ===")
        ConsoleUI.print_route(routes)
        print()
 
        while True:
            try:
                selected_route_number = ConsoleUI.get_integer_input(
                    "Wählen Sie eine Route durch Eingabe der entsprechenden Nummer",
                    1,
                    len(routes)
                )
                trip_config.select_route(routes, selected_route_number)
                print(f"Gewählte Route: {trip_config.route.name}\n")
                return
            except ValueError as e:
                print(f"{e} Bitte versuchen Sie es erneut.\n")
 
    @staticmethod
    def set_capacity_percent(trip_config):
        print("=== Batteriestand ===")
 
        while True:
            try:
                capacity_percent = ConsoleUI.get_float_input(
                    "Geben Sie den aktuellen Batteriestand in Prozent ein",
                    0,
                    100
                )
                trip_config.set_capacity_percent(capacity_percent)
                print(f"Eingegebener Batteriestand: {trip_config.capacity_percent}%\n")
                return
            except ValueError as e:
                print(f"{e} Bitte versuchen Sie es erneut.\n")