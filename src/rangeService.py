from src.check_trip_possibility import CheckTripPossibility

class RangeService:
    @staticmethod
    def calculate_energy_available_wh(trip_configuration):
        return round((trip_configuration.vehicle.capacity_kwh * 1000) * (trip_configuration.capacity_percent / 100), 2)
    
    @staticmethod
    def calculate_energy_required_wh(trip_configuration):
        general_energy_needed = trip_configuration.vehicle.average_consumption_wh_km * trip_configuration.route.distance_km
        return general_energy_needed

    @staticmethod
    def check_drive_possible(trip_configuration):
        energy_available = RangeService.calculate_energy_available_wh(trip_configuration)
        energy_required = RangeService.calculate_energy_required_wh(trip_configuration)

        tripPossibility = CheckTripPossibility()

        if(energy_available >= energy_required):
            tripPossibility.trip_possible = True
            tripPossibility.residual_capacity_wh = energy_available - energy_required
        else:
            tripPossibility.trip_possible = False
            tripPossibility.lack_capacity_wh = energy_required - energy_available

        return tripPossibility