class VehicleProfile:
    def __init__(self, name, batteriekapazitaet_kwh, durchschnittlicher_basisverbrauch_wh_km, reichweite_km, gewicht_kg):
        self.name = name
        self.batteriekapazitaet_kwh = batteriekapazitaet_kwh
        self.durchschnittlicher_basisverbrauch_wh_km = durchschnittlicher_basisverbrauch_wh_km
        self.reichweite_km = reichweite_km
        self.gewicht_kg = gewicht_kg

    def __str__(self):
        return (
            f"{self.name}: "
            f"Batteriekapazität: {self.batteriekapazitaet_kwh} kWh, "
            f"Durchschnittsverbrauch: {self.durchschnittlicher_basisverbrauch_wh_km} Wh/km, "
            f"Reichweite: {self.reichweite_km} km, "
            f"Gewicht: {self.gewicht_kg} kg"
        )