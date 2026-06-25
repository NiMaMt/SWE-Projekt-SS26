# EV Simulation Project (SS26)

The application is designed to read various electric vehicle, route, and weather profiles from JSON files. The user will be able to interactively select a vehicle, a route, and a weather profile. Additionally, the user will specify the current state of charge of the vehicle.

## Berechnung der verbleibenden Reichweite eines Autos

`RangeService.calculateEnergyAvailable`  

Input: Objekt der Klasse `TripCofiguration`  
Output: verbleibende Energie in kwh  
Berechnung: maximale Energie der Fahrzeugbatterie * Ladezustand

## Berechnung der benötigten Energie

`RangeService.calculateEnergyReqired`

## Prüfung ob Fahrt möglich ist

`RangeService.checkDrivePossible`  

Input: `TripCofiguration`  
Output: Objekt von `CheckTripPossibility`  
Aufruf von `RangeService.calculateEnergyAvailable` und `RangeService.calculateEnergyReqired` und anschließender Vergleich der verfügbaren und benötigten Energie.
Die Ergebnisse werden `CheckTripPossibility`-Objekt gespeichert.
