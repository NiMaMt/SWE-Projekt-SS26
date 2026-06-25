from src.rangeService import RangeService
from src.vehicle_profile import VehicleProfile
from src.weather_profile import WeatherProfile
from src.route_profile import RouteProfile, Segment
from src.trip_configuration import TripConfiguration

testVehicle1 = VehicleProfile(name = 'Testfahrzeug', capacity_kwh = 85, average_consumption_wh_km = 160, range_km = 531.25, weight_kg = 2100)
testSegment1 = Segment(type = "Stadt", distance_km = 8, average_speed_kmh = 35)
testSegment2 = Segment(type = "Landstraße", distance_km = 5, average_speed_kmh = 70)
testSegment3 = Segment(type = "Stadt", distance_km = 4, average_speed_kmh = 30)
testRoute1 = RouteProfile(name = "Teststrecke", start = "Esslingen am Neckar", destination = "Stuttgart", distance_km = 17, altitude_ascent = 120, altitude_descent = 95, segments = (testSegment1, testSegment2, testSegment3))
testWeatherprofile1= WeatherProfile(name = "testWetter", temperature_c = 15, rain_mm_per_h = 10, wind_speed_kmh = 20, humidity_percent = 65, weather_condition = "leicht regnerisch")
testCapacity_percent1 = 70

testTrip1 = TripConfiguration()
testTrip1.vehicle = testVehicle1
testTrip1.route = testRoute1
testTrip1.weatherprofile = testWeatherprofile1
testTrip1.capacity_percent = testCapacity_percent1

service = RangeService()

def test_check_drive_possible():
    # mehr Testcases ergänzen
    is_possible_test = service.check_drive_possible(testTrip1)
    assert(is_possible_test.trip_possible == True)

def test_calculate_energy_available():
    # mehr Testcases ergänzen

    # erwartete Rückgabe: energyAvailable = 85kwh * 70% = 59,5
    energyAvailable = service.calculate_energy_available(testTrip1)
    assert(energyAvailable == 59.5)

def test_calculate_energy_required():
    assert(True)