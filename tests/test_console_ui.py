from src.console_ui import KonsolenUI
from src.weather_profile import WeatherProfile
from src.route_profile import RouteProfile, Segment
from src.vehicle_profile import VehicleProfile

# Test Wetterausgabe in Konsole
def test_print_weather(monkeypatch, capsys):
    test_data_weather = [WeatherProfile("Sommertag", 28, 0, 12, 45, "sonnig")]

    def mock_load_weather_profile():
        return test_data_weather

    monkeypatch.setattr(
        "src.console_ui.DataLoader.load_weather_profiles",
        mock_load_weather_profile
    )

    KonsolenUI.print_weather()
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
def test_print_vehicle(monkeypatch, capsys):
    test_data_vehicle = [VehicleProfile("Ford Mustang", 600, 20, 600, 1700)]

    def mock_load_vehicle_profile():
        return test_data_vehicle

    monkeypatch.setattr(
        "src.console_ui.DataLoader.load_vehicle_profiles",
        mock_load_vehicle_profile
    )

    KonsolenUI.print_vehicle()
    captured = capsys.readouterr()

    assert "Ford Mustang" in captured.out
    assert "600 kWh" in captured.out or "600.0 kWh" in captured.out
    assert "20 Wh/km" in captured.out or "20.0 Wh/km" in captured.out
    assert "600 km" in captured.out or "600.0 km" in captured.out
    assert "1700 kg" in captured.out or "1700.0 kg" in captured.out

# Test Routenausgabe in Konsole
def test_print_route(monkeypatch, capsys):
    test_data_segment = [Segment("Landstraße", 100, 70)]
    test_data_route = [
        RouteProfile("Beispielroute", "Start", "Ziel", 300, 20, 30, test_data_segment)
    ]

    def mock_load_route_profile():
        return test_data_route

    monkeypatch.setattr(
        "src.console_ui.DataLoader.load_route_profiles",
        mock_load_route_profile
    )

    KonsolenUI.print_route()
    captured = capsys.readouterr()

    assert "Beispielroute" in captured.out
    assert "Start" in captured.out
    assert "Ziel" in captured.out
    assert "300 km" in captured.out or "300.0 km" in captured.out
    assert "20 hm" in captured.out or "20.0 hm" in captured.out
    assert "30 hm" in captured.out or "30.0 hm" in captured.out