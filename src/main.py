import data_loader as dl


def main():
    print("===========================================")
    print("Weather-aware EV Range Assistant gestartet")
    print("===========================================\n\n")

    # Test der Ausgabe von JSONFile-Inhalten
    dl.load_route_profiles()
    print("\n")
    dl.load_vehicle_profiles()
    print("\n")
    dl.load_weather_profiles()
    print("\n")
    dl.print_route_profile()
    print("\n")
    dl.print_vehicle_profile()
    print("\n")
    dl.print_weather_profile()
    print("\n")

    # Test der Funktion load_json_attributes
    dl.load_json_attributes("vehicleprofile", "name")
    dl.load_json_attributes("routeprofile", "name")
    dl.load_json_attributes("weatherprofile", "temperatur_c")
    dl.load_json_attributes("vehicleprofile", "test_falsches_attribut")
    dl.load_json_attributes("test_falscher_dateiname", "name")


if __name__ == "__main__":
    main()
