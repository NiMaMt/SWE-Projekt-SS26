class Segment:
    def __init__(self, typ, distanz_km, durchschnittsgeschwindigkeit_kmh):
        self.typ = typ
        self.distanz_km = distanz_km
        self.durchschnittsgeschwindigkeit_kmh = durchschnittsgeschwindigkeit_kmh

class RouteProfile:
    def __init__(self, name, start, ziel, gesamtdistanz_km, hoehenmeter_bergauf, hoehenmeter_bergab, segmente):
        self.name = name
        self.start = start
        self.ziel = ziel
        self.gesamtdistanz_km = gesamtdistanz_km
        self.hoehenmeter_bergauf = hoehenmeter_bergauf
        self.hoehenmeter_bergab = hoehenmeter_bergab
        self.segmente = segmente