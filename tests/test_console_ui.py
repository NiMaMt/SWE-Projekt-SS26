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

# Test get_integer_input mit gültiger Eingabe
def test_get_integer_input_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "3")

    result = ConsoleUI.get_integer_input("Wählen Sie eine Zahl", min_value=1, max_value=5)

    assert result == 3

# Test get_integer_input mit ungültiger Eingabe, dann gültiger Eingabe
def test_get_integer_input_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["abc", "0", "2"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = ConsoleUI.get_integer_input("Wählen Sie eine Zahl", min_value=1, max_value=5)
    captured = capsys.readouterr()

    assert result == 2
    assert "Ungültige Eingabe" in captured.out
    assert "Auswahlbereich" in captured.out

# Test get_float_input mit gültiger Eingabe
def test_get_float_input_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "75.5")

    result = ConsoleUI.get_float_input("Batteriestand eingeben", min_value=0, max_value=100)

    assert result == 75.5

# Test get_float_input mit ungültiger Eingabe, dann gültiger Eingabe
def test_get_float_input_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["xyz", "-5", "50.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = ConsoleUI.get_float_input("Batteriestand eingeben", min_value=0, max_value=100)
    captured = capsys.readouterr()

    assert result == 50.0
    assert "Ungültige Eingabe" in captured.out
    assert "Auswahlbereich" in captured.out

# Test get_string_choice mit gültiger Eingabe
def test_get_string_choice_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "ja")

    result = ConsoleUI.get_string_choice("Weiter?", "ja", "nein")

    assert result == "JA"

# Test get_string_choice mit ungültiger Eingabe, dann gültiger Eingabe
def test_get_string_choice_invalid_then_valid(monkeypatch, capsys):
    inputs = iter(["vielleicht", "nein"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = ConsoleUI.get_string_choice("Weiter?", "ja", "nein")
    captured = capsys.readouterr()

    assert result == "NEIN"
    assert "Bitte geben Sie" in captured.out

# Test select_vehicle mit gültiger Eingabe
def test_select_vehicle(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    vehicle = VehicleProfile("Ford Mustang", 600, 20, 600, 1700)
    config = TripConfiguration()

    ConsoleUI.select_vehicle(config, [vehicle])
    captured = capsys.readouterr()

    assert config.vehicle.name == "Ford Mustang"
    assert "Ford Mustang" in captured.out

# Test select_weather mit gültiger Eingabe
def test_select_weather(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    weather = WeatherProfile("Sommertag", 28, 0, 12, 45, "sonnig")
    config = TripConfiguration()

    ConsoleUI.select_weather(config, [weather])
    captured = capsys.readouterr()

    assert config.weather.name == "Sommertag"
    assert "Sommertag" in captured.out

# Test select_route mit gültiger Eingabe
def test_select_route(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "1")
    segments = [Segment("Landstraße", 100, 70)]
    route = RouteProfile("Beispielroute", "Start", "Ziel", 300, 20, 30, segments)
    config = TripConfiguration()

    ConsoleUI.select_route(config, [route])
    captured = capsys.readouterr()

    assert config.route.name == "Beispielroute"
    assert "Beispielroute" in captured.out

# Test set_capacity_percent mit gültiger Eingabe
def test_set_capacity_percent(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: "85")
    config = TripConfiguration()

    ConsoleUI.set_capacity_percent(config)
    captured = capsys.readouterr()

    assert config.capacity_percent == 85.0
    assert "85" in captured.out