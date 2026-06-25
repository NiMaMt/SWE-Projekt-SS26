from src.check_trip_possibility import CheckTripPossibility

class RangeService:
    @staticmethod
    def calculate_energy_available(trip_configuration):
        return round(trip_configuration.vehicle.capacity_kwh * (trip_configuration.capacity_percent / 100), 2)
    
    @staticmethod
    def calculate_energy_required(trip_configuration):
        return 0

    @staticmethod
    def check_drive_possible(trip_configuration):
        energy_available = RangeService.calculate_energy_available(trip_configuration)
        energy_required = RangeService.calculate_energy_required(trip_configuration)

        tripPossibility = CheckTripPossibility()

        if(energy_available >= energy_required):
            tripPossibility.trip_possible = True
            tripPossibility.residual_capacity_kwh = energy_available - energy_required
        else:
            tripPossibility.trip_possible = False
            tripPossibility.lack_capacity_kwh = energy_required - energy_available

        return tripPossibility