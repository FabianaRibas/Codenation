import pytest
from main import get_temperature
from unittest import mock

values = [
    (-14.235004, -51.92528, 62, 16),
    (42.3601, -71.0589, 78.76, 25),
    (-15.826691, -47.921822, 79.08, 26),
]


@pytest.mark.parametrize('lat, long, temperature, converted_temperature', values)
def test_get_temperature_by_lat_lng(lat, long, temperature, converted_temperature):

    result_json = {
        'currently': {
            'temperature': temperature
        }
    }

    with mock.patch('main.requests.get') as mk:
        mk.return_value.json.return_value = result_json
        result = get_temperature(lat, long)

    assert result == converted_temperature
