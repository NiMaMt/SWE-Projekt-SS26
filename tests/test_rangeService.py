from src.rangeService import rangeService

def test_rangeService_checkDrivePossible():
    # energyAvailable < energyReqired
    is_possible_test = rangeService.checkDrivePossible(10, 20)
    assert(is_possible_test == False)

    # energyAvailable > energyReqired
    is_possible_test = rangeService.checkDrivePossible(12, 3)
    assert(is_possible_test == True)

    # energyAvailable = energyReqired
    is_possible_test = rangeService.checkDrivePossible(50, 50)
    assert(is_possible_test == True)