import data_loader as dl


def main():
    print("===========================================")
    print("Weather-aware EV Range Assistant gestartet")
    print("===========================================\n\n")

    dl.load_route_profiles()
    dl.print_route_profile()


if __name__ == "__main__":
    main()
