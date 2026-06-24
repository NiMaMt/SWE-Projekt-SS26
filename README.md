# EV Simulation Project (SS26)

The application is designed to read various electric vehicle, route, and weather profiles from JSON files. The user will be able to interactively select a vehicle, a route, and a weather profile. Additionally, the user will specify the current state of charge of the vehicle.

## Berechnung der verbleibenden Reichweite eines Autos

`RangeService.calculateEnergyAvailable`
Input: Objekt der Klasse `VehicleProfile`, `percentageEnergyLeft`  
Output: verbleibende Energie in kwh  
Berechnung: maximale Energie der Fahrzeugbatterie * Ladezustand

## Berechnung der benötigten Energie

`RangeService.calculateEnergyReqired`

## Prüfung ob Fahrt möglich ist

`RangeService.checkDrivePossible`

Input: `energyAvailable`, `energyReqired`  
Output: true / false
Eine simple Entscheidungslogik vergleicht die verfügbare Energie und die benötigte Energie und gibt aus, ob die Fahrt so möglich ist oder nicht.
