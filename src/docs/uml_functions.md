```mermaid

---
config:
  theme: 'base'
  themeVariables:
    primaryColor: '#06a4af'
    primaryTextColor: '#fff'
    primaryBorderColor: '#000000'
    lineColor: '#dc143c'
    secondaryColor: '#08858e'
    tertiaryColor: '#fff'
---

classDiagram

    class VehicleProfile {
        +name: str
        +batteriekapazitaet_kwh: float
        +durchschnittlicher_basisverbrauch_wh_km: float
        +reichweite_km: float
        +gewicht_kg: float        
    }

    class RouteProfile {
        +name: str
        +start: str
        +ziel: str
        +gesamtdistanz_km: int
        +hoehenmeter_bergauf: int
        +hoehenmeter_bergab: int
        +segmente: int
    }

    class Segment {
        +typ: str
        +distanz_km: int
        +durchschnittsgeschwindigkeit_kmh: int
    }

    class WeatherProfile {
        +name: str
        +temperature_c: int
        +regen_mm_pro_h: float
        +windgeschwindigkeit_kmh: int
        +luftfeuchtigkeit_prozent: int
        +wetterzustand: str
    }

    class DataLoader {
        +load_weather_profiles(): List~WeatherProfile~
        +load_vehicle_profiles(): List~VehicleProfile~
        +load_route_profiles(): List~RouteProfile~
    }

    class Fahrtkonfiguration {
        +Fahrzeug fahrzeug
        +Strecke strecke
        +Wetterprofil wetterprofil
        +float ladezustandProzent
        +waehleFahrzeug(fahrzeug: Fahrzeug) void
        +waehleStrecke(strecke: Strecke) void
        +waehleWetterprofil(wetterprofil: Wetterprofil) void
        +setzeLadezustand(prozent: float) void
    }

    class ReichweitenService {
        +berechneVerfuegbareEnergie(config: Fahrtkonfiguration) float
        +berechneEnergiebedarf(config: Fahrtkonfiguration) float : farbe_ändern
        +pruefeFahrt(config: Fahrtkonfiguration) Berechnungsergebnis : farbe_ändern
    }

    class Berechnungsergebnis {
        +bool fahrtMoeglich
        +float fehlendeEnergieKWh : farbe_ändern
        +float restenergieKWh : farbe_ändern
    }

    RouteProfile "1" *-- "1...*" Segment : enthält
    
    DataLoader ..> VehicleProfile : lädt
    DataLoader ..> RouteProfile : lädt
    DataLoader ..> WeatherProfile : lädt
    Fahrtkonfiguration --> VehicleProfile
    Fahrtkonfiguration --> RouteProfile
    Fahrtkonfiguration --> WeatherProfile
    ReichweitenService --> Fahrtkonfiguration
    ReichweitenService --> Berechnungsergebnis
```