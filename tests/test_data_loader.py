from src.data_loader import DataLoader

def test_load_weather_profiles_returns_list():
    # Prüft, ob Wetterprofile als nicht-leere Liste geladen werden
    data = DataLoader.load_weather_profiles()
    assert data is not None
    assert isinstance(data, list)   # is instance. Prüft ob data eine Liste ist
    assert len(data) > 0

def test_load_weather_profiles_contains_weather_objects():
    # Prüft, ob ein Wetterprofil die erwarteten Attribute besitzt
    data = DataLoader.load_weather_profiles()
    weather = data[0]

    assert hasattr(weather, "name")  # hasattr steht für has attribute
    assert hasattr(weather, "temperature_c")
    assert hasattr(weather, "rain_mm_per_h")
    assert hasattr(weather, "wind_speed_kmh")
    assert hasattr(weather, "humidity_percent")
    assert hasattr(weather, "weather_condition")

def test_weather_profile_name_is_not_empty():
    # Prüft, ob der Name eines Wetterprofils sinnvoll befüllt ist
    data = DataLoader.load_weather_profiles()
    weather = data[0]

    assert isinstance(weather.name, str)
    assert weather.name != ""    # Prüft ob name leer ist

def test_load_vehicle_profiles_returns_list():
    # Prüft, ob Fahrzeugprofile als nicht-leere Liste geladen werden
    data = DataLoader.load_vehicle_profiles()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0

def test_load_vehicle_profiles_contains_vehicle_objects():
    # Prüft, ob ein Fahrzeugprofil die erwarteten Attribute besitzt
    data = DataLoader.load_vehicle_profiles()
    vehicle = data[0]

    assert hasattr(vehicle, "name")
    assert hasattr(vehicle, "capacity_kwh")
    assert hasattr(vehicle, "average_consumption_wh_km")
    assert hasattr(vehicle, "range_km")
    assert hasattr(vehicle, "weight_kg")

def test_load_vehicle_profiles_loads_multiple_entries():
    # Prüft, ob mehr als ein Fahrzeugprofil geladen wird
    data = DataLoader.load_vehicle_profiles()

    assert len(data) > 1

def test_load_route_profiles_returns_list():
    # Prüft, ob Streckenprofile als nicht-leere Liste geladen werden
    data = DataLoader.load_route_profiles()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0

def test_load_route_profiles_contains_route_objects():
    # Prüft, ob ein Streckenprofil die erwarteten Attribute besitzt
    data = DataLoader.load_route_profiles()
    route = data[0]

    assert hasattr(route, "name")   
    assert hasattr(route, "start")
    assert hasattr(route, "destination")
    assert hasattr(route, "distance_km")
    assert hasattr(route, "altitude_ascent")
    assert hasattr(route, "altitude_descent")
    assert hasattr(route, "segments")

def test_route_profile_contains_segment_list():
    # Prüft, ob eine Route eine nicht-leere Segmentliste enthält
    data = DataLoader.load_route_profiles()
    route = data[0]

    assert isinstance(route.segments, list)
    assert len(route.segments) > 0

def test_route_segments_have_expected_attributes():
    # Prüft, ob ein Segment die erwarteten Attribute besitzt
    data = DataLoader.load_route_profiles()
    route = data[0]
    segment = route.segments[0]

    assert hasattr(segment, "type")
    assert hasattr(segment, "distance_km")
    assert hasattr(segment, "average_speed_kmh")

def test_route_segment_values_are_valid():
    # Prüft, ob die Werte eines Segments sinnvoll befüllt sind
    data = DataLoader.load_route_profiles()
    route = data[0]
    segment = route.segments[0]

    assert isinstance(segment.type, str)
    assert segment.type != ""
    assert segment.distance_km > 0
    assert segment.average_speed_kmh > 0