class WeatherProfile:
    def __init__(self, name, temperature_c, rain_mm_per_h, wind_speed_kmh, humidity_percent, weather_condition):
        self.name = name
        self.temperature_c = temperature_c
        self.rain_mm_per_h = rain_mm_per_h
        self.wind_speed_kmh = wind_speed_kmh
        self.humidity_percent = humidity_percent
        self.weather_condition = weather_condition

    def __str__(self):
        return (
            f"{self.name}: "
            f"{self.temperature_c} °C, "
            f"{self.rain_mm_per_h} mm/h, "
            f"{self.wind_speed_kmh} km/h, "
            f"{self.humidity_percent}%, "
            f"Zustand: {self.weather_condition}"
        )