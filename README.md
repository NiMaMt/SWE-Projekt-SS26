# Weather-aware EV Range Assistant

## Semesterbegleitendes Projekt Software Engineering (SoSe 2026)

## Kurzbeschreibung

Der "Weather-aware EV Range Assistant" ist eine Softwareanwendung, die entwickelt wurde, um die Machbarkeit einer geplanten Fahrt mit einem Elektrofahrzeug zu bewerten. Sie berücksichtigt dabei verschiedene Faktoren wie Fahrzeugtyp, Streckenprofil und aktuelle Wetterbedingungen. Die Anwendung lädt Fahrzeug-, Strecken- und Wetterprofile aus JSON-Dateien, ermöglicht dem Benutzer eine interaktive Auswahl und berechnet auf Basis des aktuellen Ladezustands, ob die Fahrt erfolgreich absolviert werden kann. Bei Nicht-Machbarkeit wird der fehlende Energiebedarf oder der mindestens erforderliche Start-Ladezustand angezeigt.

Der Fokus dieses Projekts liegt auf einer sauberen Softwarearchitektur, verständlichen Anforderungen, UML-Modellierung, Versionskontrolle und der Dokumentation der zugrundeliegenden Annahmen, anstatt auf einer physikalisch perfekten Reichweitenberechnung.

---

## Funktionsbeschreibung der Berechnungsfunktionen

Die Kernlogik der Reichweitenberechnung ist in der `RangeService`-Klasse gekapselt. Die folgenden Abschnitte beschreiben die einzelnen Berechnungsfunktionen und die zugrundeliegenden Annahmen.

### Berechnung der verbleibenden Reichweite eines Autos

`RangeService.calculateEnergyAvailable`

*   **Input:** Objekt der Klasse `TripConfiguration`
*   **Output:** verbleibende Energie in kWh
*   **Berechnung:** maximale Energie der Fahrzeugbatterie * Ladezustand

### Berechnung der benötigten Energie

`RangeService.calculateEnergyRequired`

Energiebedarf grundsätzlich = Fahrzeugverbrauch pro Strecke * geplante Strecke

Weitere Faktoren abhängig von verschiedenen Parametern:

#### Art der Strecke

*   Faktor Stadt -> 1.10
*   Faktor Landstraße -> 0.95
*   Faktor Autobahn -> 1.20

#### Geschwindigkeit auf Streckenabschnitten

*   Faktor 30 km/h -> 1.05
*   Faktor 50 km/h -> 1.00
*   Faktor 70 km/h -> 1.03
*   Faktor 90 km/h -> 1.08
*   Faktor 120 km/h -> 1.20
*   Faktor 150 km/h -> 1.45

#### Höhenmeter hoch

Umrechnung in Lageenergie, die zusätzlich aufgebracht werden muss mit:
$$E = m \cdot g \cdot h$$
Umrechnung in kWh mit /3600

#### Höhenmeter bergab

Nutzung der Lageenergie zur Rekuperation unter Berücksichtigung der Effizienz (Bsp. 65%)

#### Temperatur

Mehrverbrauch für Heizung / Klimaanlage + ggf. Batterie heizen:
$$0,5h \cdot \text{Energiebedarf/h} + (\text{Fahrtzeit} - 0,5h) \cdot 0,5 \cdot \text{Energiebedarf/h}$$

*   \>30°C -> 2,5 kWh/h
*   30-20°C -> 1 kWh/h
*   10–20°C -> 0,3 kWh/h
*   0–10°C -> 2 kWh/h
*   -10–0°C -> 3,5 kWh/h
*   <-10°C -> 5 kWh/h

#### Regen

Erhöhter Rollwiderstand durch Wasser auf der Fahrbahn:
$$\text{Regenfaktor} = 1 + \text{Niederschlag in mm/h} \cdot 0,005$$
ergibt:

*   0 mm/h -> 1.00
*   4 mm/h -> 1.02
*   10 mm/h -> 1.05
*   16 mm/h -> 1.08

### Prüfung ob Fahrt möglich ist

`RangeService.checkDrivePossible`

*   **Input:** `TripConfiguration`
*   **Output:** Objekt von `CheckTripPossibility`
*   **Logik:** Aufruf von `RangeService.calculateEnergyAvailable` und `RangeService.calculateEnergyRequired` und anschließender Vergleich der verfügbaren und benötigten Energie. Die Ergebnisse werden im `CheckTripPossibility`-Objekt gespeichert.

---

## Build- und Startanleitung


### Klonen des Repositorys

Um die Anwendung nutzen zu können, muss zunächst das Repository geklont werden.

**Klone das Repository:**
    Öffne dein Terminal oder deine Kommandozeile und klone das Projekt von GitHub, gib dazu die folgenden Befehle ein:
    
    git clone https://github.com/NiMaMt/SWE-Projekt-SS26.git
    cd SWE-Projekt-SS26

### Starten der Anwendung

Nachdem das Repository erfolgreich geklont wurde, kannst du die Anwendung über die Konsole wie folgt starten:

```bash
python main.py
```
## Beispiele zur Verwendung

Im Folgenden werden zwei Beispielausgaben der Konsole dargestellt, die den interaktiven Ablauf und die Ergebnisse der Reichweitenberechnung zeigen: einmal mit ausreichender Reichweite und einmal mit nicht ausreichender Reichweite.


Nach dem Start der Anwendung in deinem Terminal wirst du interaktiv durch den Prozess geführt. Die Anwendung fordert dich auf, ein Fahrzeug, ein Wetterprofil und eine Route auszuwählen, gefolgt von der Eingabe des aktuellen Batterieladezustands in Prozent.

```bash
# Beispiel 1: Fahrt möglich

In diesem Beispiel wird ein Audi A6 Sportback e-tron mit 80% Ladung bei heißem Sommerwetter auf der Route Stuttgart -> München simuliert. Die Anwendung bestätigt, dass die Fahrt möglich ist.

================================
Weather-aware EV Range Assistant
================================


Lade Fahrzeugdaten...
Lade Wetterdaten...
Lade Routendaten...
Alle Daten erfolgreich geladen.

=== Fahrzeugauswahl ===
Nr. Name                                     Kapazität      Verbrauch    Reichweite     Gewicht
-----------------------------------------------------------------------------------------------
1   Kia EV3                                   78.0 kWh     171.0 Wh/km     455.0 km    1885.0 kg
2   Volkswagen ID.Polo                        51.7 kWh     154.0 Wh/km     335.0 km    1576.0 kg
3   BMW iX3 50 xDrive                        108.7 kWh     171.0 Wh/km     635.0 km    2360.0 kg
4   Tesla Model Y Maximale Reichweite AWD     72.0 kWh     169.0 Wh/km     425.0 km    2056.0 kg
5   Tesla Model 3 RWD                         60.0 kWh     133.0 Wh/km     450.0 km    1847.0 kg
6   Tesla Model 3 Premium RWD                 79.0 kWh     136.0 Wh/km     580.0 km    1822.0 kg
7   Audi A6 Sportback e-tron                  75.8 kWh     156.0 Wh/km     485.0 km    2175.0 kg
8   Tesla Model Y RWD                         57.0 kWh     165.0 Wh/km     345.0 km    1992.0 kg
9   Mercedes-Benz CLA 250+                    85.0 kWh     145.0 Wh/km     585.0 km    2055.0 kg
10  Škoda Epiq 55                             51.7 kWh     162.0 Wh/km     320.0 km    1618.0 kg

Wählen Sie ein Fahrzeug durch Eingabe der entsprechenden Nummer: 7
Gewähltes Fahrzeug: Audi A6 Sportback e-tron

=== Wetterauswahl ===
Nr. Name                             Temp.       Regen        Wind    Luftf.   Zustand
--------------------------------------------------------------------------------------
1   Sonniger Sommertag              28.0 °C     0.0 mm/h    12.0 km/h  45.0%   sonnig
2   Leichter Regen                  17.0 °C     2.5 mm/h    20.0 km/h  78.0%   regnerisch
3   Starker Regen und Wind          11.0 °C     9.8 mm/h    55.0 km/h  92.0%   sturm
4   Winterliche Bedingungen         -3.0 °C     1.2 mm/h    25.0 km/h  85.0%   schnee
5   Bewölkter Herbsttag              9.0 °C     0.4 mm/h    18.0 km/h  70.0%   bewölkt
6   Nebliger Morgen                  6.0 °C     0.0 mm/h     5.0 km/h  96.0%   nebel
7   Heißer Sommertag                34.0 °C     0.0 mm/h    10.0 km/h  35.0%   heiß
8   Gewitter                        21.0 °C    14.5 mm/h    70.0 km/h  88.0%   gewitter

Wählen Sie ein Wetter durch Eingabe der entsprechenden Nummer: 7
Gewähltes Wetter: Heißer Sommertag

=== Routenauswahl ===
Nr. Name                               Start                  Ziel                        Distanz    +Höhenm.    -Höhenm.
-------------------------------------------------------------------------------------------------------------------------
1   Esslingen am Neckar -> Stuttgart   Esslingen am Neckar    Stuttgart                     17 km      120 m       95 m
2   Reutlingen -> Ulm                  Reutlingen             Ulm                           95 km      420 m      380 m
3   Stuttgart -> Munich                Stuttgart              München                      220 km      760 m      690 m
4   Freudenstadt -> Stuttgart          Freudenstadt           Stuttgart                     90 km      540 m      710 m
5   Darmstadt -> Frankfurt am Main     Darmstadt              Frankfurt am Main             35 km      110 m      140 m
6   Frankfurt am Main -> Cologne       Frankfurt am Main      Köln                         190 km      680 m      640 m
7   Berlin -> Hanover                  Berlin                 Hannover                     285 km      320 m      300 m
8   Hannover -> Hamburg                Hannover               Hamburg                      155 km      180 m      170 m
9   Stuttgart -> Berlin                Stuttgart              Berlin                       635 km     1250 m     1180 m
10  München -> Hamburg                 München                Hamburg                      780 km     1480 m     1420 m

Wählen Sie eine Route durch Eingabe der entsprechenden Nummer: 3
Gewählte Route: Stuttgart -> Munich

=== Batteriestand ===
Geben Sie den aktuellen Batteriestand in Prozent ein: 80
Eingegebener Batteriestand: 80.0%

=== Konfiguration abgeschlossen ===
=== Ihre gewählte Konfiguration ===

Fahrzeug   : Audi A6 Sportback e-tron
Reichweite : 485.0 km

Route      : Stuttgart -> Munich
Distanz    : 220 km

Wetter     : Heißer Sommertag
Temperatur : 34 °C
Zustand    : heiß

Ladestatus : 80.0 %
=== Routenberechnung ===
Ihre Route wird berechnet...
Die Fahrt ist mit Ihrem aktuellen Batteriestand möglich
Erwartete Restkapazität am Ziel: 7.46 kWh
```

```bash
# Beispiel 2: Fahrt NICHT möglich

In diesem Beispiel wird ein Škoda Epiq 55 mit 20% Ladung bei einem bewölktem Herbsttag auf der Route München -> Hamburg simuliert. Die Anwendung bestätigt, dass die Fahrt NICHT möglich ist.

================================
Weather-aware EV Range Assistant
================================


Lade Fahrzeugdaten...
Lade Wetterdaten...
Lade Routendaten...
Alle Daten erfolgreich geladen.

=== Fahrzeugauswahl ===
Nr. Name                                     Kapazität      Verbrauch    Reichweite     Gewicht
-----------------------------------------------------------------------------------------------
1   Kia EV3                                   78.0 kWh     171.0 Wh/km     455.0 km    1885.0 kg
2   Volkswagen ID.Polo                        51.7 kWh     154.0 Wh/km     335.0 km    1576.0 kg
3   BMW iX3 50 xDrive                        108.7 kWh     171.0 Wh/km     635.0 km    2360.0 kg
4   Tesla Model Y Maximale Reichweite AWD     72.0 kWh     169.0 Wh/km     425.0 km    2056.0 kg
5   Tesla Model 3 RWD                         60.0 kWh     133.0 Wh/km     450.0 km    1847.0 kg
6   Tesla Model 3 Premium RWD                 79.0 kWh     136.0 Wh/km     580.0 km    1822.0 kg
7   Audi A6 Sportback e-tron                  75.8 kWh     156.0 Wh/km     485.0 km    2175.0 kg
8   Tesla Model Y RWD                         57.0 kWh     165.0 Wh/km     345.0 km    1992.0 kg
9   Mercedes-Benz CLA 250+                    85.0 kWh     145.0 Wh/km     585.0 km    2055.0 kg
10  Škoda Epiq 55                             51.7 kWh     162.0 Wh/km     320.0 km    1618.0 kg

Wählen Sie ein Fahrzeug durch Eingabe der entsprechenden Nummer: 10
Gewähltes Fahrzeug: Škoda Epiq 55

=== Wetterauswahl ===
Nr. Name                             Temp.       Regen        Wind    Luftf.   Zustand
--------------------------------------------------------------------------------------
1   Sonniger Sommertag              28.0 °C     0.0 mm/h    12.0 km/h  45.0%   sonnig
2   Leichter Regen                  17.0 °C     2.5 mm/h    20.0 km/h  78.0%   regnerisch
3   Starker Regen und Wind          11.0 °C     9.8 mm/h    55.0 km/h  92.0%   sturm
4   Winterliche Bedingungen         -3.0 °C     1.2 mm/h    25.0 km/h  85.0%   schnee
5   Bewölkter Herbsttag              9.0 °C     0.4 mm/h    18.0 km/h  70.0%   bewölkt
6   Nebliger Morgen                  6.0 °C     0.0 mm/h     5.0 km/h  96.0%   nebel
7   Heißer Sommertag                34.0 °C     0.0 mm/h    10.0 km/h  35.0%   heiß
8   Gewitter                        21.0 °C    14.5 mm/h    70.0 km/h  88.0%   gewitter

Wählen Sie ein Wetter durch Eingabe der entsprechenden Nummer: 5
Gewähltes Wetter: Bewölkter Herbsttag

=== Routenauswahl ===
Nr. Name                               Start                  Ziel                        Distanz    +Höhenm.    -Höhenm.
-------------------------------------------------------------------------------------------------------------------------
1   Esslingen am Neckar -> Stuttgart   Esslingen am Neckar    Stuttgart                     17 km      120 m       95 m
2   Reutlingen -> Ulm                  Reutlingen             Ulm                           95 km      420 m      380 m
3   Stuttgart -> Munich                Stuttgart              München                      220 km      760 m      690 m
4   Freudenstadt -> Stuttgart          Freudenstadt           Stuttgart                     90 km      540 m      710 m
5   Darmstadt -> Frankfurt am Main     Darmstadt              Frankfurt am Main             35 km      110 m      140 m
6   Frankfurt am Main -> Cologne       Frankfurt am Main      Köln                         190 km      680 m      640 m
7   Berlin -> Hanover                  Berlin                 Hannover                     285 km      320 m      300 m
8   Hannover -> Hamburg                Hannover               Hamburg                      155 km      180 m      170 m
9   Stuttgart -> Berlin                Stuttgart              Berlin                       635 km     1250 m     1180 m
10  München -> Hamburg                 München                Hamburg                      780 km     1480 m     1420 m

Wählen Sie eine Route durch Eingabe der entsprechenden Nummer: 10
Gewählte Route: München -> Hamburg

=== Batteriestand ===
Geben Sie den aktuellen Batteriestand in Prozent ein: 20
Eingegebener Batteriestand: 20.0%

=== Konfiguration abgeschlossen ===
=== Ihre gewählte Konfiguration ===

Fahrzeug   : Škoda Epiq 55
Reichweite : 320.0 km

Route      : München -> Hamburg
Distanz    : 780 km

Wetter     : Bewölkter Herbsttag
Temperatur : 9 °C
Zustand    : bewölkt

Ladestatus : 20.0 %
=== Routenberechnung ===
Ihre Route wird berechnet...
!ACHTUNG! Das Erreichen des Ziels ist mit Ihrem aktuellen Batteriestand NICHT möglich
Fehlende Kapazität: 179.58 kWh
```
