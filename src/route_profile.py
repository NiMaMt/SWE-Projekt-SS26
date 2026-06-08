class Segment:
    def __init__(self, typ, distanz_km, durchschnittsgeschwindigkeit_kmh):
        self.typ = typ
        self.distanz_km = distanz_km
        self.durchschnittsgeschwindigkeit_kmh = durchschnittsgeschwindigkeit_kmh

    def __str__(self):
        return (
            f"{self.typ}, "
            f"{self.distanz_km} km, "
            f"Durchschnittsgeschwindigkeit: {self.durchschnittsgeschwindigkeit_kmh} km/h"
        )

class RouteProfile:
    def __init__(self, name, start, ziel, gesamtdistanz_km, hoehenmeter_bergauf, hoehenmeter_bergab, segmente):
        self.name = name
        self.start = start
        self.ziel = ziel
        self.gesamtdistanz_km = gesamtdistanz_km
        self.hoehenmeter_bergauf = hoehenmeter_bergauf
        self.hoehenmeter_bergab = hoehenmeter_bergab
        self.segmente = segmente

    def __str__(self):
        # Wandelt jedes Segment nur für die Ausgabe in einen String um und fügt alle mit ", " zusammen;
        # Die Werte in self.segmente bleiben unverändert, z. B. bleibt 100 weiterhin ein Zahlenwert im Segment-Objekt
        segmente_text = ", ".join(str(segment) for segment in self.segmente)
        return (
            f"{self.name}: "
            f"Startort: {self.start}, "
            f"Zielort: {self.ziel}, "
            f"Gesamtdistanz: {self.gesamtdistanz_km} km, "
            f"{self.hoehenmeter_bergauf} hm, "
            f"{self.hoehenmeter_bergab} hm, "
            f"Segmente: {segmente_text}"
        )