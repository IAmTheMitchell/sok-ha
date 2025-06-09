from types import SimpleNamespace

import pytest

from custom_components.sok import async_remove_config_entry_device
from custom_components.sok.const import DOMAIN


class DummyHass:
    pass


class DummyRegistry:
    def __init__(self):
        self.removed = None

    def async_remove_device(self, device_id: str) -> None:
        self.removed = device_id


@pytest.mark.asyncio
async def test_remove_config_entry_device(monkeypatch):
    hass = DummyHass()
    entry = SimpleNamespace(unique_id="00:11:22:33:44:55")
    registry = DummyRegistry()
    monkeypatch.setattr("custom_components.sok.dr.async_get", lambda _: registry)
    device = SimpleNamespace(
        id="device1", identifiers={(DOMAIN, "00:11:22:33:44:55")}
    )

    result = await async_remove_config_entry_device(hass, entry, device)

    assert result is True
    assert registry.removed == "device1"
