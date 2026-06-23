from src.data_loader import DataLoader


def test_load_weather_profiles_returns_list():
    # Checks if weather profiles are loaded as a non-empty list
    data = DataLoader.load_weather_profiles()
    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0

def test_load_weather_profiles_contains_weather_objects():
    # Checks if a weather profile has the expected attributes
    data = DataLoader.load_weather_profiles()
    weather = data[0]

    assert hasattr(weather, "name")
    assert hasattr(weather, "temperature_c") # Updated
    assert hasattr(weather, "rain_mm_per_h") # Updated
    assert hasattr(weather, "wind_speed_kmh") # Updated
    assert hasattr(weather, "humidity_percent") # Updated
    assert hasattr(weather, "weather_condition") # Updated

def test_weather_profile_name_is_not_empty():
    # Checks if the name of a weather profile is meaningfully populated
    data = DataLoader.load_weather_profiles()
    weather = data[0]

    assert isinstance(weather.name, str)
    assert weather.name != ""

def test_load_vehicle_profiles_returns_list():
    # Checks if vehicle profiles are loaded as a non-empty list
    data = DataLoader.load_vehicle_profiles()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0

def test_load_vehicle_profiles_contains_vehicle_objects():
    # Checks if a vehicle profile has the expected attributes
    data = DataLoader.load_vehicle_profiles()
    vehicle = data[0]

    assert hasattr(vehicle, "name")
    assert hasattr(vehicle, "battery_capacity_kwh") # Updated
    assert hasattr(vehicle, "average_consumption_wh_km") # Updated
    assert hasattr(vehicle, "range_km") # Updated
    assert hasattr(vehicle, "weight_kg") # Updated

def test_load_vehicle_profiles_loads_multiple_entries():
    # Checks if more than one vehicle profile is loaded
    data = DataLoader.load_vehicle_profiles()

    assert len(data) > 1

def test_load_route_profiles_returns_list():
    # Checks if route profiles are loaded as a non-empty list
    data = DataLoader.load_route_profiles()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0

def test_load_route_profiles_contains_route_objects():
    # Checks if a route profile has the expected attributes
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
    # Checks if a route contains a non-empty list of segments
    data = DataLoader.load_route_profiles()
    route = data[0]

    assert isinstance(route.segments, list) 
    assert len(route.segments) > 0

def test_route_segments_have_expected_attributes():
    # Checks if a segment has the expected attributes
    data = DataLoader.load_route_profiles()
    route = data[0]
    segment = route.segments[0] 
    assert hasattr(segment, "type") 
    assert hasattr(segment, "distance_km") 
    assert hasattr(segment, "average_speed_kmh") 

def test_route_segment_values_are_valid():
    # Checks if the values of a segment are meaningfully populated
    data = DataLoader.load_route_profiles()
    route = data[0]
    segment = route.segments[0] # Updated

    assert isinstance(segment.type, str) # Updated
    assert segment.type != ""
    assert segment.distance_km > 0 # Updated
    assert segment.average_speed_kmh > 0 # Updated