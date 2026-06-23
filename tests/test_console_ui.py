from src.console_ui import ConsoleUI
from src.weather_profile import WeatherProfile
from src.route_profile import RouteProfile, Segment
from src.vehicle_profile import VehicleProfile

# Test Weather Output in Console
def test_print_weather(monkeypatch, capsys):
    test_data_weather = [WeatherProfile("Sunny Day", 28, 0, 12, 45, "sunny")]

    def mock_load_weather_profile():
        return test_data_weather
    
    monkeypatch.setattr("src.console_ui.DataLoader.load_weather_profiles", mock_load_weather_profile)
    ConsoleUI.print_weather()
    captured = capsys.readouterr()

    expected_output = (
        "Nr. Name                             Temp.        Rain        Wind Humidity.   Condition\n"
        "----------------------------------------------------------------------------------------\n"
        "1   Sunny Day                       28.0 °C     0.0 mm/h    12.0 km/h  45.0%   sunny\n"
    )
    assert captured.out == expected_output

# Test Vehicle Output in Console
def test_print_vehicle(monkeypatch, capsys):
    test_data_vehicle = [VehicleProfile("Ford Mustang", 600.0, 20.0, 600.0, 1700.0)]
    def mock_load_vehicle_profile():
        return test_data_vehicle
    
    monkeypatch.setattr("src.console_ui.DataLoader.load_vehicle_profiles", mock_load_vehicle_profile)
    ConsoleUI.print_vehicle()
    captured = capsys.readouterr()

    expected_output = (
        "Nr. Name                                       Battery    Consumption         Range      Weight\n"
        "-----------------------------------------------------------------------------------------------\n"
        "1   Ford Mustang                             600.0 kWh      20.0 Wh/km     600.0 km   1700.0 kg\n"
    )
    assert captured.out == expected_output

# Test Route Output in Console
def test_print_route(monkeypatch, capsys):
    test_data_segment = [Segment("Country Road", 100, 70)] 
    test_data_route = [RouteProfile("Example Route", "Start", "Destination", 300, 20, 30, test_data_segment)]
    
    def mock_load_route_profile():
        return test_data_route
    
    monkeypatch.setattr("src.console_ui.DataLoader.load_route_profiles", mock_load_route_profile)
    ConsoleUI.print_route()
    captured = capsys.readouterr()

    expected_output = (
        "Nr. Name                               Start                  Destination                Distance      Ascent     Descent\n"
        "-------------------------------------------------------------------------------------------------------------------------\n"
        "1   Example Route                      Start                  Destination                  300 km       20 hm       30 hm\n" 
    )
    assert captured.out == expected_output