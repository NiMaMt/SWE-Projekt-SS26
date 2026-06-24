from src.rangeService import rangeService
from src.vehicle_profile import VehicleProfile

def test_rangeService_checkDrivePossible():
    # energyAvailable < energyReqired
    is_possible_test = rangeService.checkDrivePossible(energyAvailable=10, energyReqired=20)
    assert(is_possible_test == False)

    # energyAvailable > energyReqired
    is_possible_test = rangeService.checkDrivePossible(energyAvailable=12, energyReqired=3)
    assert(is_possible_test == True)

    # energyAvailable = energyReqired
    is_possible_test = rangeService.checkDrivePossible(energyAvailable=50, energyReqired=50)
    assert(is_possible_test == True)

def test_rangeService_calculateEnergyAvailable():
    testVehicle = VehicleProfile(name = 'Testvehicle', capacity_kwh = 85, average_consumption_wh_km = 160, range_km = 531.25, weight_kg = 2100)

    energyAvailable = rangeService.calculateEnergyAvailable(testVehicle, 0.6)
    assert(energyAvailable == 100)