""" Gather static agency/route/stop data """
import os
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

class Seattle:
    def __init__(
        self,
        api_key: str = os.environ['API_KEY'],
        api: str = os.environ['API']
    ) -> None:
        self.api_key = api_key
        self.api = api
        self.session = Session()
        retries = Retry(
            total=3,
            backoff_factor=10,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods={'GET'}
        )
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def request(self, route: str, **kwargs):
        payload = {
            'key': self.api_key
        }
        for key, value in kwargs.items():
            payload[key] = value
        endpoint = self.api + route
        try:
            response = self.session.get(endpoint, params=payload)
            response.raise_for_status()
            response_json = response.json()
            self.last_updated = response_json['currentTime']
            return response_json
        except Exception as _:
            # TODO: better error handling
            print('Issue')

    @property
    def last_updated(self) -> int:
        return self._last_updated

    @last_updated.setter
    def last_updated(self, update_time: int) -> None:
        self._last_updated = update_time

    @last_updated.deleter
    def last_updated(self) -> None:
        del self._last_updated

    def get_trips(self, route_id: str) -> list[str]:
        response = self.request(f'trips-for-route/{route_id}.json', includeSchedule=False)
        trip_list = response['data']['list']
        return trip_list
