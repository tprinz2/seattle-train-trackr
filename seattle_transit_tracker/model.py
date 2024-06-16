""" Data model for transportation system """
from dataclasses import dataclass, field

type Routes = dict[str, Route]
type Stops = dict[str, Stop]
type RGB = tuple[int, int, int]

@dataclass
class LED:
    id: str
    _color: RGB = (0, 0, 0)

    @property
    def color(self) -> RGB:
        return self._color

    @color.setter
    def color(self, rgb: RGB) -> None:
        self._color = rgb

@dataclass
class Stop:
    id: int
    name: str
    direction: str
    led: LED

@dataclass
class Route:
    id: int
    name: str
    _stops: Stops = field(default_factory=dict)

    @property
    def stops(self) -> Stops:
        return self._stops

    @stops.setter
    def stops(self, new_stops: Stops) -> None:
        self._stops = new_stops

@dataclass
class Agency:
    id: int
    name: str
    _routes: Routes = field(default_factory=dict)

    @property
    def routes(self) -> Routes:
        return self._routes

    @routes.setter
    def routes(self, new_routes: Routes) -> None:
        self._routes = new_routes