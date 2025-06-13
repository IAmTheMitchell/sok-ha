from types import SimpleNamespace
from datetime import timedelta

import pytest

from custom_components.sok_battery.sensor import SOKEnergySensor
from homeassistant.util import dt as dt_util


class DummyCoordinator:
    def __init__(self, device):
        self.data = device
        self.address = "00:11:22:33:44:55"
        self.entry = SimpleNamespace(title="Battery", unique_id=self.address)
        self.unique_id = self.entry.unique_id


def test_energy_in_sensor(monkeypatch):
    start = dt_util.utcnow()
    device = SimpleNamespace(voltage=12.0, current=5.0)
    coordinator = DummyCoordinator(device)
    sensor = SOKEnergySensor(coordinator, key="energy_in", name="Energy In", direction="in")
    sensor._last_update = start
    # hass is None so _handle_coordinator_update won't write state
    monkeypatch.setattr(dt_util, "utcnow", lambda: start + timedelta(hours=1))
    sensor._handle_coordinator_update()
    assert pytest.approx(sensor.native_value, rel=1e-3) == 0.06


def test_energy_out_sensor(monkeypatch):
    start = dt_util.utcnow()
    device = SimpleNamespace(voltage=12.0, current=-5.0)
    coordinator = DummyCoordinator(device)
    sensor = SOKEnergySensor(coordinator, key="energy_out", name="Energy Out", direction="out")
    sensor._last_update = start
    # hass is None so _handle_coordinator_update won't write state
    monkeypatch.setattr(dt_util, "utcnow", lambda: start + timedelta(hours=2))
    sensor._handle_coordinator_update()
    assert pytest.approx(sensor.native_value, rel=1e-3) == 0.12
