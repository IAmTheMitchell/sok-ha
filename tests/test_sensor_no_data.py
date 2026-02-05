from types import SimpleNamespace
from typing import cast

import pytest

from custom_components.sok_battery.coordinator import SOKDataUpdateCoordinator
from custom_components.sok_battery.sensor import SENSOR_DESCRIPTIONS, SOKSensorEntity


class DummyCoordinator:
    def __init__(self, data=None):
        self.data = data
        self.address = "00:11:22:33:44:55"
        self.entry = SimpleNamespace(title="Battery", unique_id=self.address)
        self.unique_id = self.entry.unique_id


@pytest.mark.asyncio
async def test_native_value_no_data():
    coordinator = cast(SOKDataUpdateCoordinator, DummyCoordinator(None))
    sensor = SOKSensorEntity(coordinator, SENSOR_DESCRIPTIONS[0])
    assert sensor.native_value is None
