from src.data_loader import DataLoader


class ConsoleUI:

    @staticmethod
    def format_weather_list(data):
        header = (
        f"{'Nr.':<4}"
        f"{'Name':<30}"
        f"{'Temp.':>8}"
        f"{'Rain':>12}"
        f"{'Wind':>12}"
        f"{'Humidity.':>10}"
        f"   Condition")
        
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
    def print_weather():
        data_weather = DataLoader.load_weather_profiles()
        print(ConsoleUI.format_weather_list(data_weather))

    @staticmethod
    def format_vehicle_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Name':<38}"
            f"{'Battery':>12}"
            f"{'Consumption':>15}"
            f"{'Range':>14}"
            f"{'Weight':>12}"
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
                f" {item.weight_kg:>8.1f} kg"
            )

        return "\n".join(rows)

    @staticmethod
    def print_vehicle():
        data_vehicles = DataLoader.load_vehicle_profiles()
        print(ConsoleUI.format_vehicle_list(data_vehicles))

    @staticmethod
    def format_route_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Name':<35}"
            f"{'Start':<23}"
            f"{'Destination':<23}"
            f"{'Distance':>12}"
            f"{'Ascent':>12}"
            f"{'Descent':>12}"
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
                f"{item.altitude_ascent:>9} hm"
                f"{item.altitude_descent:>9} hm"
            )

        return "\n".join(rows)

    @staticmethod
    def print_route():
        data_routes = DataLoader.load_route_profiles()
        print(ConsoleUI.format_route_list(data_routes))

    @staticmethod
    def format_segment_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Type of Route':<12}"
            f"{'Length':<12}"
            f"{'Average speed':<4}"
        )

        separation_line = "-" * len(header)
        rows = [header, separation_line]

        for nummer, item in enumerate(data, start=1):
            rows.append(
                f"{nummer:<4}"
                f"{item.type:<12}"
                f"{f'{item.distance_km} km' :<12}"
                f"{f'{item.average_speed_kmh} km/h':<4}"
            )

        return "\n".join(rows)
    
    # Achtung. Hier Objekt von RoutenProfil übergeben
    @staticmethod
    def print_segment(route):
        print(ConsoleUI.format_segment_list(route.segments))
