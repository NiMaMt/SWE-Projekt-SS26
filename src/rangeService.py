class rangeService:
    def calculateEnergyAvailable(vehicle, percentageEnergyLeft): # Funktion zur Hilfsfunktion von checkDrivePossible machen und nur notwendige Parameter übergeben?
        return vehicle.capacity_kwh * percentageEnergyLeft
    
    def calculate_energy_required(): # Funktion zur Hilfsfunktion von checkDrivePossible machen und nur notwendige Parameter übergeben?
        return 0

    def checkDrivePossible(energyAvailable, energyReqired): # müsste TripConfiguration erhalten (und calculateEnergyAvailable und calculate_energy_required aufrufen?)
        if(energyAvailable >= energyReqired):
            return True # Rückgabewert müsste vom Typ check_trip_possibility sein
        else:
            return False
