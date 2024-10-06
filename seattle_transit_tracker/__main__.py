""" Seattle Train Tracker main loop """
import time
import board
import neopixel
from .data import Seattle
from .model import SoundTransit

# Initialize LEDs
ioPin   = board.D18
numLeds = 6
ORDER   = neopixel.GRB
leds    = neopixel.NeoPixel(ioPin, numLeds, brightness=0.1,
                            auto_write=False, pixel_order=ORDER)

# TODO: There should be a better way to define a relationship between N/S for same station
stationStatusList = [[False, False], [False, False], [False, False],
                     [False, False], [False, False], [False, False] ]

START_TIME = time.monotonic()
SEATTLE    = Seattle()

while True:
    for route in SoundTransit.routes.keys():
        trips = SEATTLE.get_trips(route)
        stop_ids: list[str] = []
        for trip in trips:
            closest_stop_id = trip['status']['closestStop']
            stop_ids.append(closest_stop_id)
        for stop_id, stop in SoundTransit.routes[route].stops.items():
            if stop_id in stop_ids:
                stop.hasTrain = True
            else:
                stop.hasTrain = False

    for route in SoundTransit.routes.values():
        for key, value in route.stops.items():
            match value.id:
                # TODO: This should be cleaner - at least have defines
                # Also need to print out stations in order (N/S grouped)

                # Westlake
                case "40_1121":
                    stationStatusList[0][0] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)
                case "40_1108":
                    stationStatusList[0][1] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)

                # Capitol Hill
                case "40_99603":
                    stationStatusList[1][0] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)
                case "40_99610":
                    stationStatusList[1][1] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)

                # UW
                case "40_99605":
                    stationStatusList[2][0] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)
                case "40_99604":
                    stationStatusList[2][1] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)

                # U District
                case "40_990002":
                    stationStatusList[3][0] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)
                case "40_990001":
                    stationStatusList[3][1] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)

                # Roosevelt
                case "40_990004":
                    stationStatusList[4][0] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)
                case "40_990003":
                    stationStatusList[4][1] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)

                # Northgate
                case "40_990006":
                    stationStatusList[5][0] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)
                case "40_990005":
                    stationStatusList[5][1] = value.hasTrain
                    print(value.name, value.direction, value.hasTrain)

    for index, station in enumerate(stationStatusList):
        if station[0] and station[1]:
            leds[index] = (255, 0, 255)
        elif station[0]:
            leds[index] = (255, 0, 0)
        elif station[1]:
            leds[index] = (0, 0, 255)
        else:
            leds[index] = (0, 0, 0)

    leds.show()
    print('\n')
    time.sleep(60)
