from src.console_ui import ConsoleUI
from src.weather_profile import WeatherProfile
from src.route_profile import RouteProfile, Segment
from src.vehicle_profile import VehicleProfile
from src.trip_configuration import TripConfiguration

# Test Weather Output in Console
def test_print_weather(capsys):
    test_data_weather = [WeatherProfile("Sommertag", 28, 0, 12, 45, "sonnig")]

    ConsoleUI.print_weather(test_data_weather)
    captured = capsys.readouterr()

    assert "Nr." in captured.out
    assert "Name" in captured.out
    assert "Sommertag" in captured.out
    assert "28.0 °C" in captured.out
    assert "0.0 mm/h" in captured.out
    assert "12.0 km/h" in captured.out
    assert "45.0%" in captured.out
    assert "sonnig" in captured.out

# Test Fahrzeugausgabe in Konsole
def test_print_vehicle(capsys):
    test_data_vehicle = [VehicleProfile("Ford Mustang", 600, 20, 600, 1700)]

    ConsoleUI.print_vehicle(test_data_vehicle)
    captured = capsys.readouterr()

    assert "Ford Mustang" in captured.out
    assert "600 kWh" in captured.out or "600.0 kWh" in captured.out
    assert "20 Wh/km" in captured.out or "20.0 Wh/km" in captured.out
    assert "600 km" in captured.out or "600.0 km" in captured.out
    assert "1700 kg" in captured.out or "1700.0 kg" in captured.out

# Test Route Output in Console
def test_print_route(capsys):
    test_data_segment = [Segment("Landstraße", 100, 70)]
    test_data_route = [
        RouteProfile("Beispielroute", "Start", "Ziel", 300, 20, 30, test_data_segment)
    ]

    ConsoleUI.print_route(test_data_route)
    captured = capsys.readouterr()

    assert "Beispielroute" in captured.out
    assert "Start" in captured.out
    assert "Ziel" in captured.out
    assert "300 km" in captured.out or "300.0 km" in captured.out
    assert "20 hm" in captured.out or "20.0 hm" in captured.out
    assert "30 hm" in captured.out or "30.0 hm" in captured.out

# Test ausgewählte Konfiguration in Konsole
def test_print_selected_configuration(capsys):
    vehicle = VehicleProfile("Ford Mustang", 600, 20, 600, 1700)
    weather = WeatherProfile("Sommertag", 28, 0, 12, 45, "sonnig")
    segments = [Segment("Landstraße", 100, 70)]
    route = RouteProfile("Beispielroute", "Start", "Ziel", 300, 20, 30, segments)

    # Hier nochmal getestet, ob das klappt mit dem erzeugen eines Objektes
    config = TripConfiguration()
    config.select_vehicle([vehicle], 1)
    config.select_route([route], 1)
    config.select_weather([weather], 1)
    config.set_capacity_percent(80)

    ConsoleUI.print_selected_configuration(config)
    captured = capsys.readouterr()

    assert "Ford Mustang" in captured.out
    assert "600 km" in captured.out or "600.0 km" in captured.out
    assert "Beispielroute" in captured.out
    assert "300 km" in captured.out or "300.0 km" in captured.out
    assert "Sommertag" in captured.out
    assert "28" in captured.out or "28.0" in captured.out
    assert "sonnig" in captured.out
    assert "80" in captured.out or "80.0" in captured.out