class Segment:
    def __init__(self, type, distance_km, average_speed_kmh):
        self.type = type
        self.distance_km = distance_km
        self.average_speed_kmh = average_speed_kmh

    def __str__(self):
        return (
            f"{self.type}, "
            f"{self.distance_km} km, "
            f"Average speed: {self.average_speed_kmh} km/h"
        )

class RouteProfile:
    def __init__(self, name, start, destination, distance_km, altitude_ascent, altitude_descent, segments):
        self.name = name
        self.start = start
        self.destination = destination
        self.distance_km = distance_km
        self.altitude_ascent = altitude_ascent
        self.altitude_descent = altitude_descent
        self.segments = segments

    def __str__(self):
        # Converts each segment to a string for output and joins them with ", ";
        # The values in self.segments remain unchanged, e.g., 100 still remains a numerical value in the Segment object.
        segments_text = ", ".join(str(segment) for segment in self.segments)
        return (
            f"{self.name}: "
            f"Starting point: {self.start}, "
            f"Destination: {self.destination}, "
            f"Full Distance: {self.distance_km} km, "
            f"{self.altitude_ascent} hm, "
            f"{self.altitude_descent} hm, "
            f"Segments: {segments_text}"
        )