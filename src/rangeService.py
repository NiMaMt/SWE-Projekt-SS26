from src.check_trip_possibility import CheckTripPossibility

G = float(9.81) # Erdbeschleunigung in m/s^2
FACTOR_J_TO_WH = 3600 # Umrechnungsfaktor Joule in Wh
RECUPERATION_EFFICIENCY = float(0.65) # 65%

class RangeService:
    @staticmethod
    def calculate_energy_available_wh(trip_configuration):
        return round((trip_configuration.vehicle.capacity_kwh * 1000) * (trip_configuration.capacity_percent / 100), 2)
    
    @staticmethod
    def calculate_energy_required_wh(trip_configuration):
        #general_energy_needed = trip_configuration.vehicle.average_consumption_wh_km * trip_configuration.route.distance_km

        road_dependent_energy_factors = {
            "Stadt" : 1.10,
            "Landstraße" : 0.95,
            "Autobahn" : 1.20
        }

        speed_dependent_energy_factors = {  # Geschwindigkeit in km/h
            30 : 1.05,  
            50 : 1.00,
            70 : 1.03,
            90 : 1.08,
            120 : 1.20,
            150 : 1.45
        }

        temperature_dependent_energy_val = {
        # Temp. : Energiebedarf in W
            35 : 2500,  
            25 : 1000,  
            15 : 300,
            5 : 2000,
            -5 : 3500,
            -15 : 5000
        }

        energy_required = 0

        for segment in trip_configuration.route.segments:
            segment_energy_required = trip_configuration.vehicle.average_consumption_wh_km * segment.distance_km

            road_type_factor = road_dependent_energy_factors[segment.type]

            speed_factor_key = min(speed_dependent_energy_factors, key = lambda k: abs(k - segment.average_speed_kmh))
            speed_factor = speed_dependent_energy_factors[int(speed_factor_key)]

            energy_required += segment_energy_required * road_type_factor * speed_factor

        # Höhenmeterbetrachtung:
        # Umrechnung in Lageenergie, die zusätzlich aufgebracht werden muss mit E=m * g * h  
        # Umrechnung in kWh mit /3600
        energy_required_uphill = trip_configuration.vehicle.weight_kg * G * trip_configuration.route.altitude_ascent / FACTOR_J_TO_WH
        energy_required += energy_required_uphill

        # Höhenmeter bergab (rekuperation):
        # m * g * h * Effizienz
        # Umrechnung in kWh mit /3600
        energy_gain_downhill = trip_configuration.vehicle.weight_kg * G * trip_configuration.route.altitude_descent * RECUPERATION_EFFICIENCY / FACTOR_J_TO_WH
        energy_required -= energy_gain_downhill



        return round(energy_required, 2)

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