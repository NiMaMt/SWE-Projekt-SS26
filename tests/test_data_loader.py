import src.data_loader as dl    # Merkwürdige Syntax, aber nur import src.data_loader geht nicht

# Test - Laden der Wetterprofile aus weatherprofile.json
def test_load_weather_profiles_returns_data():
    data = dl.load_weather_profiles()

    assert data is not None
    assert "wetterprofile" in data
    assert len(data["wetterprofile"]) > 0

# Test - Laden der Fahrzeugprofile aus vehicleprofile.json
def test_load_vehicle_profiles_returns_data():
    data = dl.load_vehicle_profiles()

    assert data is not None
    assert "fahrzeugprofile" in data
    assert len(data["fahrzeugprofile"]) > 0

# Test - Laden der Streckenprofile aus routeprofile.json
def test_load_route_profiles_returns_data():
    data = dl.load_route_profiles()

    assert data is not None
    assert "streckenprofile" in data
    assert len(data["streckenprofile"]) > 0

# Test - Ausgabe Wetterprofil
def test_print_weather_profile():

    data = dl.load_weather_profiles()
    assert len(data) > 0