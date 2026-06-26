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
testTrip1.weather = testWeatherprofile1
testTrip1.capacity_percent = testCapacity_percent1

service = RangeService()

def test_check_drive_possible():
    # mehr Testcases ergänzen
    is_possible_test = service.check_drive_possible(testTrip1)
    assert(is_possible_test.trip_possible == True)

def test_calculate_energy_available_wh():
    # mehr Testcases ergänzen

    # erwartete Rückgabe: energyAvailable = 85kwh * 70% = 59500 Wh
    energyAvailable = service.calculate_energy_available_wh(testTrip1)
    assert(energyAvailable == 59500)

def test_calculate_energy_required_wh():
    energy_required = service.calculate_energy_required_wh(testTrip1)
    # erwartet:
    # Strecke,          Straßentyp, Geschwindigkeit (je Segment):
    # 160Wh/km * 8km    * 1,1       * 1,05
    # + 160Wh/km * 5km  * 0,95      * 1,03
    # + 160Wh * 4km     * 1,1       * 1,05 = 3000,4Wh
    # 
    # Höhenmeter:
    # m        * g         * h      (Umrechnung in Wh)
    # + 2100kg * 9,81m/s^2 * 120m / 3600 = 686,7Wh
    #
    #--------------------------------------------------
    #                                    = 3687,1
    assert(energy_required == 3687.1)