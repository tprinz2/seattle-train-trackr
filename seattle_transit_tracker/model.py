""" Data model for transportation system """
from dataclasses import dataclass, field

@dataclass
class Stop:
    id: int
    name: str
    direction: str
    hasTrain: bool

@dataclass
class Route:
    id: int
    name: str
    _stops: dict[str, Stop] = field(default_factory=dict)

    @property
    def stops(self) -> dict[str, Stop]:
        return self._stops

    @stops.setter
    def stops(self, new_stops: dict[str, Stop]) -> None:
        self._stops = new_stops

@dataclass
class Agency:
    id: int
    name: str
    _routes: dict[str, Route] = field(default_factory=dict)

    @property
    def routes(self) -> dict[str, Route]:
        return self._routes

    @routes.setter
    def routes(self, new_routes: dict[str, Route]) -> None:
        self._routes = new_routes

# routes and stops won't change often, so simply hardcode
link1_stops = {
    '40_1108': Stop('40_1108', 'Westlake', 'SW', False),
    '40_1121': Stop('40_1121', 'Westlake', 'NE', False),
    '40_455': Stop('40_455', 'University St', 'SE', False),
    '40_501': Stop('40_501', 'Pioneer Square', 'SE', False),
    '40_532': Stop('40_532', 'Pioneer Square', 'NW', False),
    '40_55578': Stop('40_55578', 'Rainier Beach', 'N', False),
    '40_55656': Stop('40_55656', 'Othello', 'NW', False),
    '40_55778': Stop('40_55778', 'Columbia City', 'NW', False),
    '40_55860': Stop('40_55860', 'Mount Baker', 'NW', False),
    '40_55949': Stop('40_55949', 'Mount Baker', 'SE', False),
    '40_56039': Stop('40_56039', 'Columbia City', '', False),
    '40_56159': Stop('40_56159', 'Othello', 'SE', False),
    '40_56173': Stop('40_56173', 'Rainier Beach', 'S', False),
    '40_565': Stop('40_565', 'University St', 'NW', False),
    '40_621': Stop('40_621', "Int'l Dist/Chinatown", 'N', False),
    '40_623': Stop('40_623', "Int'l Dist/Chinatown", 'S', False),
    '40_990001': Stop('40_990001', 'U District', 'S', False),
    '40_990002': Stop('40_990002', 'U District', 'N', False),
    '40_990003': Stop('40_990003', 'Roosevelt', 'S', False),
    '40_990004': Stop('40_990004', 'Roosevelt', 'N', False),
    '40_990005': Stop('40_990005', 'Northgate', '', False),
    '40_990006': Stop('40_990006', 'Northgate', '', False),
    '40_99101': Stop('40_99101', 'Stadium', 'S', False),
    '40_99111': Stop('40_99111', 'SODO', '', False),
    '40_99121': Stop('40_99121', 'Beacon Hill', 'E', False),
    '40_99240': Stop('40_99240', 'Beacon Hill', 'W', False),
    '40_99256': Stop('40_99256', 'SODO', 'N', False),
    '40_99260': Stop('40_99260', 'Stadium', 'N', False),
    '40_99603': Stop('40_99603', 'Capitol Hill', 'N', False),
    '40_99604': Stop('40_99604', 'Univ of Washington', 'S', False),
    '40_99605': Stop('40_99605', 'Univ of Washington', 'N', False),
    '40_99610': Stop('40_99610', 'Capitol Hill', 'S', False),
    '40_99900': Stop('40_99900', "Tukwila Int'l Blvd", 'W', False),
    '40_99903': Stop('40_99903', "SeaTac/Airport", '', False),
    '40_99904': Stop('40_99904', "SeaTac/Airport", '', False),
    '40_99905': Stop('40_99905', "Tukwila Int'l Blvd", 'E', False),
    '40_99913': Stop('40_99913', 'Angle Lake', '', False),
    '40_99914': Stop('40_99914', 'Angle Lake', '', False)
}
Link1Line = Route('40_100479', 'Link 1 Line')
Link1Line.stops = link1_stops

link2_stops = {
    '40_E09-T2': Stop('40_E09-T2', 'South Bellevue', '', False),
    '40_E11-T1': Stop('40_E11-T1', 'East Main', 'S', False),
    '40_E11-T2': Stop('40_E11-T2', 'East Main', 'N', False),
    '40_E15-T1': Stop('40_E15-T1', 'Bellevue Downtown', 'W', False),
    '40_E15-T2': Stop('40_E15-T2', 'Bellevue Downtown', 'E', False),
    '40_E19-T1': Stop('40_E19-T1', 'Wilburton', 'S', False),
    '40_E19-T2': Stop('40_E19-T2', 'Wilburton', 'N', False),
    '40_E21-T1': Stop('40_E21-T1', 'Spring District', 'W', False),
    '40_E21-T2': Stop('40_E21-T2', 'Spring District', 'E', False),
    '40_E23-T1': Stop('40_E23-T1', 'BelRed', 'W', False),
    '40_E23-T2': Stop('40_E23-T2', 'BelRed', 'E', False),
    '40_E25-T1': Stop('40_E25-T1', 'Overlake Village', 'SW', False),
    '40_E25-T2': Stop('40_E25-T2', 'Overlake Village', 'NE', False),
    '40_E27-T1': Stop('40_E27-T1', 'Redmond Technology', '', False),
    '40_E27-T2': Stop('40_E27-T2', 'Redmond Technology', '', False)
}
Link2Line = Route('40_2LINE', 'Link 2 Line')
Link2Line.stops = link2_stops

SoundTransit = Agency(40, 'Sound Transit')
SoundTransit.routes = {
    '40_100479': Link1Line,
    '40_2LINE': Link2Line
}
