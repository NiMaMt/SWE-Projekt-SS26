from dataclasses import dataclass

@dataclass
class CheckTripPossibility:
    trip_possible: bool = False
    lack_capacity_wh: float = 0.0
    residual_capacity_wh: float = 0.0