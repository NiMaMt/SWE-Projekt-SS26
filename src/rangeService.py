class rangeService:
    def calculateEnergyAvailable(vehicle, percentageEnergyLeft):
        return vehicle.capacity_kwh * percentageEnergyLeft

    def checkDrivePossible(energyAvailable, energyReqired):
        if(energyAvailable >= energyReqired):
            return True
        else:
            return False
