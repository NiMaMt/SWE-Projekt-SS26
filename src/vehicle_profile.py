class VehicleProfile:
    def __init__(self, name, battery_capacity_kwh, average_consumption_wh_km, range_km, weight_kg):
        self.name = name
        self.battery_capacity_kwh = battery_capacity_kwh
        self.average_consumption_wh_km = average_consumption_wh_km
        self.range_km = range_km
        self.weight_kg = weight_kg

    def __str__(self):
        return (
            f"{self.name}: "
            f"Battery Capacity: {self.battery_capacity_kwh} kWh, "
            f"Average Consumption: {self.average_consumption_wh_km} Wh/km, "
            f"Range: {self.range_km} km, "
            f"Weight: {self.weight_kg} kg"
        )