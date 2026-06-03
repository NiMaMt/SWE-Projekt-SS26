``` mermaid

classDiagram
    class RouteProfile {
        +name: string
        +start: string
        +ziel: string
        +gesamtdistanz_km: int
        +hoehenmeter_bergauf: int
        +hoehenmeter_bergab: int
        +segmente: int
    }

    class Segment {
        +typ: string
        +distanz_km: int
        +durchschnittsgeschwindigkeit_kmh: int
    }

    class VehicleProfile {
        +name: string
        +batteriekapazitaet_kwh: float
        +durchschnittlicher_basisverbrauch_wh_km: float
        +reichweite_km: float
        +gewicht_kg: float        
    }

    class WeatherProfile {
        +name: string
        +temperature_c: int
        +regen_mm_pro_h: float
        +windgeschwindigkeit_kmh: int
        +luftfeuchtigkeit_prozent: int
        +wetterzustand: string
    }

RouteProfile "1" *-- "1...*" Segment : enthält

```