class WeatherProfile:
    def __init__(self, name, temperatur_c, regen_mm_pro_h, windgeschwindigkeit_kmh, luftfeuchtigkeit_prozent, wetterzustand):
        self.name = name
        self.temperatur_c = temperatur_c
        self.regen_mm_pro_h = regen_mm_pro_h
        self.windgeschwindigkeit_kmh = windgeschwindigkeit_kmh
        self.luftfeuchtigkeit_prozent = luftfeuchtigkeit_prozent
        self.wetterzustand = wetterzustand

    def __str__(self):
        return (
            f"{self.name}: "
            f"{self.temperatur_c} °C, "
            f"{self.regen_mm_pro_h} mm/h, "
            f"{self.windgeschwindigkeit_kmh} km/h, "
            f"{self.luftfeuchtigkeit_prozent}%, "
            f"Zustand: {self.wetterzustand}"
        )