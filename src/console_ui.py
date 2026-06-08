from src.data_loader import DataLoader


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
        f"   Zustand")
        
        trennlinie = "-" * len(header)
        zeilen = [header, trennlinie]

        for nummer, item in enumerate(data, start=1):
            zeilen.append(
                f"{nummer:<4}"
                f"{item.name:<30}"
                f"{item.temperatur_c:>6.1f} °C"
                f"{item.regen_mm_pro_h:>8.1f} mm/h"
                f"{item.windgeschwindigkeit_kmh:>8.1f} km/h"
                f"{item.luftfeuchtigkeit_prozent:>6.1f}%"
                f"   {item.wetterzustand}"
            )

        return "\n".join(zeilen)

    @staticmethod
    def print_weather():
        daten_wetter = DataLoader.load_weather_profiles()
        print(ConsoleUI.format_weather_list(daten_wetter))

    @staticmethod
    def format_vehicle_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Name':<38}"
            f"{'Batterie':>12}"
            f"{'Verbrauch':>15}"
            f"{'Reichweite':>14}"
            f"{'Gewicht':>12}"
        )

        trennlinie = "-" * len(header)
        zeilen = [header, trennlinie]

        for nummer, item in enumerate(data, start=1):
            zeilen.append(
                f"{nummer:<4}"
                f"{item.name:<38}"
                f"{item.batteriekapazitaet_kwh:>8.1f} kWh"
                f"{item.durchschnittlicher_basisverbrauch_wh_km:>10.1f} Wh/km"
                f"{item.reichweite_km:>10.1f} km"
                f" {item.gewicht_kg:>8.1f} kg"
            )

        return "\n".join(zeilen)

    @staticmethod
    def print_vehicle():
        daten_fahrzeuge = DataLoader.load_vehicle_profiles()
        print(ConsoleUI.format_vehicle_list(daten_fahrzeuge))

    @staticmethod
    def format_route_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Name':<35}"
            f"{'Start':<23}"
            f"{'Ziel':<23}"
            f"{'Distanz':>12}"
            f"{'Bergauf':>12}"
            f"{'Bergab':>12}"
        )

        trennlinie = "-" * len(header)
        zeilen = [header, trennlinie]

        for nummer, item in enumerate(data, start=1):
            zeilen.append(
                f"{nummer:<4}"
                f"{item.typ:<35}"
                f"{item.start:<23}"
                f"{item.ziel:<23}"
                f"{item.gesamtdistanz_km:>9} km"
                f"{item.hoehenmeter_bergauf:>9} hm"
                f"{item.hoehenmeter_bergab:>9} hm"
            )

        return "\n".join(zeilen)

    @staticmethod
    def print_route():
        daten_routen = DataLoader.load_route_profiles()
        print(ConsoleUI.format_route_list(daten_routen))

    @staticmethod
    def format_segment_list(data):
        header = (
            f"{'Nr.':<4}"
            f"{'Streckenart':<12}"
            f"{'Länge':<12}"
            f"{'Durchschnittsgeschw.':<4}"
        )

        trennlinie = "-" * len(header)
        zeilen = [header, trennlinie]

        for nummer, item in enumerate(data, start=1):
            zeilen.append(
                f"{nummer:<4}"
                f"{item.typ:<12}"
                f"{f'{item.distanz_km} km' :<12}"
                f"{f'{item.durchschnittsgeschwindigkeit_kmh} km/h':<4}"
            )

        return "\n".join(zeilen)
    
    # Achtung. Hier Objekt von RoutenProfil übergeben
    @staticmethod
    def print_segment(route):
        print(ConsoleUI.format_segment_list(route.segmente))