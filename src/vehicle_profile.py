class VehicleProfile:
    def __init__(self, name, capacity_kwh, average_consumption_wh_km, range_km, weight_kg):
        self.name = name
        self.capacity_kwh = capacity_kwh
        self.average_consumption_wh_km = average_consumption_wh_km
        self.range_km = range_km
        self.weight_kg = weight_kg

    def __str__(self):
        return (
            f"{self.name}: "
            f"Batteriekapazität: {self.capacity_kwh} kWh, "
            f"Durchschnittsverbrauch: {self.average_consumption_wh_km} Wh/km, "
            f"Reichweite: {self.range_km} km, "
            f"Gewicht: {self.weight_kg} kg"
        )