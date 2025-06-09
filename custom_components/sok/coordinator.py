"""Coordinator for polling SOK BLE batteries."""

from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.components.bluetooth import async_ble_device_from_address
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import (
    CONNECTION_BLUETOOTH,
    DeviceInfo,
)
from homeassistant.helpers.update_coordinator import (
    DataUpdateCoordinator,
    UpdateFailed,
)

from sok_ble.sok_bluetooth_device import SokBluetoothDevice
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

UPDATE_INTERVAL = timedelta(minutes=3)


class SOKDataUpdateCoordinator(DataUpdateCoordinator[SokBluetoothDevice]):
    """Coordinator to manage polling the SOK battery."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        self.entry = entry
        self.address = entry.unique_id
        super().__init__(
            hass,
            _LOGGER,
            name="SOK BLE",
            update_interval=UPDATE_INTERVAL,
        )
        self.data: SokBluetoothDevice | None = None

    @property
    def unique_id(self) -> str:
        """Return a unique id for this coordinator."""
        return self.entry.unique_id or getattr(self.entry, "entry_id", self.address)

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information for the battery."""
        return DeviceInfo(
            identifiers={(DOMAIN, self.unique_id)},
            connections={(CONNECTION_BLUETOOTH, self.address)},
            name=getattr(self.entry, "title", self.address),
            manufacturer="SOK",
        )

    async def _async_update_data(self) -> SokBluetoothDevice:
        assert self.address is not None
        ble_device = async_ble_device_from_address(
            self.hass, self.address, connectable=True
        )
        if not ble_device:
            raise UpdateFailed(f"Device {self.address} not found")
        device = SokBluetoothDevice(ble_device)
        try:
            await device.async_update()
        except Exception as err:
            raise UpdateFailed(err) from err
        self.data = device
        return device
