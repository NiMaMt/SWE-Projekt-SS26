# EV Simulation Project (SS26)

The application is designed to read various electric vehicle, route, and weather profiles from JSON files. The user will be able to interactively select a vehicle, a route, and a weather profile. Additionally, the user will specify the current state of charge of the vehicle.

## Berechnung der verbleibenden Reichweite eines Autos

`RangeService.calculateEnergyAvailable`  

Input: Objekt der Klasse `TripCofiguration`  
Output: verbleibende Energie in kwh  
Berechnung: maximale Energie der Fahrzeugbatterie * Ladezustand

## Berechnung der benötigten Energie

`RangeService.calculateEnergyReqired`

Energiebedarf grundsätzlich = Fahrzeugverbrauch pro Strecke * geplante Stecke

Weitere Faktoren abhängig von verschiedenen Parametern:
### Art der Strecke:
Faktor Stadt -> 1.10
Faktor Landstraße -> 0.95
Faktor Autobahn -> 1.20

### Geschwindigkeit auf Streckenabschnitten:
Faktor 30 km/h -> 1.05  
Faktor 50 km/h -> 1.00  
Faktor 70 km/h -> 1.03  
Faktor 90 km/h -> 1.08  
Faktor 120 km/h -> 1.20  
Faktor 150 km/h -> 1.45  

### Höhenmeter hoch:
Umrechnung in Lageenergie, die zusätzlich aufgebracht werden muss mit E=m⋅g⋅h  
Umrechnung in kWh mit /3600

### Höhenmeter bergab:
Nutzung der Lageenergie zur Rekuperation unter Berücksichtigung der Effizienz (Bsp.65%)

### Temperatur:
Mehrverbrauch für Heizung / Klimaanlage + ggf. Batterie heizen:  
0,5h von Fahrtzeit \* Energiebedarf/h + Fahrtzeit -0.5h \* Energiebedarf/h  
\>30°C -> 2,5 kWh/h  
30-20°C -> 1 kWh/h  
10–20°C -> 0,3 kWh/h  
0–10°C -> 2 kWh/h  
-10–0°C -> 3,5 kWh/h  
<-10°C -> 5 kWh/h  

### Regen:
Erhöhter Rollwiderstand durch Wasser auf der Fahrbahn:  
Regenfaktor = 1 + Niederschlag in mm/h \* 0,005  
ergibt:  
0 mm/h    -> 1.00  
4 mm/h    -> 1.02  
10 mm/h   -> 1.05  
16 mm/h   -> 1.08  

## Prüfung ob Fahrt möglich ist

`RangeService.checkDrivePossible`  

Input: `TripCofiguration`  
Output: Objekt von `CheckTripPossibility`  
Aufruf von `RangeService.calculateEnergyAvailable` und `RangeService.calculateEnergyReqired` und anschließender Vergleich der verfügbaren und benötigten Energie.
Die Ergebnisse werden `CheckTripPossibility`-Objekt gespeichert.
