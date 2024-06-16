""" Seattle Train Tracker main loop """
import time
from .data import Seattle
from .model import SoundTransit

START_TIME = time.monotonic()
SEATTLE = Seattle()

while True:
    for route in SoundTransit.routes.keys():
        trips = SEATTLE.get_trips(route)
        stop_ids: list[str] = []
        for trip in trips:
            closest_stop_id = trip['status']['closestStop']
            stop_ids.append(closest_stop_id)
        for stop_id, stop in SoundTransit.routes[route].stops.items():
            if stop_id in stop_ids:
                stop.led.color = (255, 255, 255)
            else:
                stop.led.color = (0, 0, 0)

    # TODO: address LEDs instead of printing
    for route in SoundTransit.routes.values():
        for key, value in route.stops.items():
            print(key, ': ', value.led.color)
    print('\n')
    time.sleep(60.0 - ((time.monotonic() - START_TIME) % 60.0))