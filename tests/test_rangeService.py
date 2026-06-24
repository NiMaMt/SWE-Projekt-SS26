from src.rangeService import rangeService

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