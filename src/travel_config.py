from src.data_loader import DataLoader
from src.console_ui import KonsolenUI
from src.vehicle_profile import VehicleProfile


class Fahrtkonfiguration:
    fahrzeug = VehicleProfile()

    wahl_fahrzeug = input("Bitte wählen Sie ein Fahrzeug durch Eingabe der Nr.: ")
    