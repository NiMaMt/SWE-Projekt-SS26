from src.console_ui import ConsoleUI
from src.weather_profile import WeatherProfile
from src.route_profile import RouteProfile, Segment
from src.vehicle_profile import VehicleProfile

# Test Wetterausgabe in Konsole
def test_print_weather(monkeypatch, capsys):
    # Um nicht die komplette JSON zu vergleichen, hier eine Mock Liste für einen Eintrag
    test_data_weather = [WeatherProfile("Sommertag", 28, 0, 12, 45, "sonnig") ]

    def mock_load_weather_profile():
        return test_data_weather
    
    monkeypatch.setattr("src.console_ui.DataLoader.load_weather_profiles", mock_load_weather_profile)
    ConsoleUI.print_weather()

    # Fängt die Ausgabe ab
    captured = capsys.readouterr()
    # Das ist die erwartete Ausgabe
    assert captured.out == "1. Sommertag: 28 °C, 0 mm/h Regen, 12 km/h Wind, 45% Luftfeuchtigkeit, Zustand: sonnig\n"

# Test Fahrzeugausgabe in Konsole
def test_print_vehicle(monkeypatch, capsys):
    test_data_vehicle = [VehicleProfile("Ford Mustang", 600, 20, 600, 1700)]
    def mock_load_vehicle_profile():
        return test_data_vehicle
    
    monkeypatch.setattr("src.console_ui.DataLoader.load_vehicle_profiles", mock_load_vehicle_profile)
    ConsoleUI.print_vehicle()
    captured = capsys.readouterr()
    assert captured.out == "1. Ford Mustang: Batteriekapazität: 600 kWh, Durchschnittsverbrauch: 20 Wh/km, Reichweite: 600 km, Gewicht: 1700 kg\n"

# Test Routenausgabe in Konsole
def test_print_route(monkeypatch, capsys):
    test_data_segment = [Segment("Landstraße", 100, 70)]
    test_data_route = [RouteProfile("Beispielroute", "Start", "Ziel", 300, 20, 30, test_data_segment)]
    def mock_load_route_profile():
        return test_data_route
    
    monkeypatch.setattr("src.console_ui.DataLoader.load_route_profiles", mock_load_route_profile)
    ConsoleUI.print_route()
    captured = capsys.readouterr()
    assert captured.out == "1. Beispielroute: Startort: Start, Zielort: Ziel, Gesamtdistanz: 300 km, +20 hm, -30 hm, Segmente: Landstraße, 100 km, Durchschnittsgeschwindigkeit: 70 km/h\n"