import asyncio
from types import SimpleNamespace

import pytest
from bleak.backends.device import BLEDevice

from custom_components.sok_battery.coordinator import SOKDataUpdateCoordinator


class DummyHass:
    def __init__(self):
        self.loop = asyncio.get_event_loop()


@pytest.mark.asyncio
async def test_async_update(monkeypatch):
    hass = DummyHass()
    entry = SimpleNamespace(unique_id="00:11:22:33:44:55")
    coordinator = SOKDataUpdateCoordinator(hass, entry)

    device = BLEDevice("00:11:22:33:44:55", "SOK-AA", None, -60)

    def fake_ble_device_from_address(hass, address, connectable=True):
        return device

    async def fake_async_update(self):
        self.voltage = 12.5
        self.current = 5.0
        self.soc = 80
        self.temperature = 25.0
        self.capacity = 100.0
        self.num_cycles = 10
        self.cell_voltages = [3.3, 3.3, 3.3, 3.3]

    monkeypatch.setattr(
        "custom_components.sok_battery.coordinator.async_ble_device_from_address",
        fake_ble_device_from_address,
    )
    monkeypatch.setattr(
        "sok_ble.sok_bluetooth_device.SokBluetoothDevice.async_update",
        fake_async_update,
    )

    device_obj = await coordinator._async_update_data()
    assert device_obj.voltage == 12.5
    assert coordinator.data.voltage == 12.5
