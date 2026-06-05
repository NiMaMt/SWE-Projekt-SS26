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
    wetter = data[0]

    assert hasattr(wetter, "name")  # hasattr steht für has attribute
    assert hasattr(wetter, "temperatur_c")
    assert hasattr(wetter, "regen_mm_pro_h")
    assert hasattr(wetter, "windgeschwindigkeit_kmh")
    assert hasattr(wetter, "luftfeuchtigkeit_prozent")
    assert hasattr(wetter, "wetterzustand")

def test_weather_profile_name_is_not_empty():
    # Prüft, ob der Name eines Wetterprofils sinnvoll befüllt ist
    data = DataLoader.load_weather_profiles()
    wetter = data[0]

    assert isinstance(wetter.name, str)
    assert wetter.name != ""    # Prüft ob name leer ist

def test_load_vehicle_profiles_returns_list():
    # Prüft, ob Fahrzeugprofile als nicht-leere Liste geladen werden
    data = DataLoader.load_vehicle_profiles()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0

def test_load_vehicle_profiles_contains_vehicle_objects():
    # Prüft, ob ein Fahrzeugprofil die erwarteten Attribute besitzt
    data = DataLoader.load_vehicle_profiles()
    fahrzeug = data[0]

    assert hasattr(fahrzeug, "name")
    assert hasattr(fahrzeug, "batteriekapazitaet_kwh")
    assert hasattr(fahrzeug, "durchschnittlicher_basisverbrauch_wh_km")
    assert hasattr(fahrzeug, "reichweite_km")
    assert hasattr(fahrzeug, "gewicht_kg")

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
    assert hasattr(route, "ziel")
    assert hasattr(route, "gesamtdistanz_km")
    assert hasattr(route, "hoehenmeter_bergauf")
    assert hasattr(route, "hoehenmeter_bergab")
    assert hasattr(route, "segmente")

def test_route_profile_contains_segment_list():
    # Prüft, ob eine Route eine nicht-leere Segmentliste enthält
    data = DataLoader.load_route_profiles()
    route = data[0]

    assert isinstance(route.segmente, list)
    assert len(route.segmente) > 0

def test_route_segments_have_expected_attributes():
    # Prüft, ob ein Segment die erwarteten Attribute besitzt
    data = DataLoader.load_route_profiles()
    route = data[0]
    segment = route.segmente[0]

    assert hasattr(segment, "typ")
    assert hasattr(segment, "distanz_km")
    assert hasattr(segment, "durchschnittsgeschwindigkeit_kmh")

def test_route_segment_values_are_valid():
    # Prüft, ob die Werte eines Segments sinnvoll befüllt sind
    data = DataLoader.load_route_profiles()
    route = data[0]
    segment = route.segmente[0]

    assert isinstance(segment.typ, str)
    assert segment.typ != ""
    assert segment.distanz_km > 0
    assert segment.durchschnittsgeschwindigkeit_kmh > 0