"""The SOK Bluetooth integration."""

from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr

from .const import DOMAIN
from .coordinator import SOKDataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)

SOKConfigEntry = ConfigEntry[SOKDataUpdateCoordinator]

PLATFORMS: list[Platform] = [Platform.SENSOR]


async def async_setup_entry(hass: HomeAssistant, entry: SOKConfigEntry) -> bool:
    """Set up SOK BLE device from a config entry."""
    assert entry.unique_id is not None
    battery_name = getattr(entry, "title", entry.unique_id)
    _LOGGER.debug("Setting up SOK battery %s", battery_name)
    coordinator = SOKDataUpdateCoordinator(hass, entry)

    async def first_refresh() -> None:
        try:
            await coordinator.async_config_entry_first_refresh()
        except ConfigEntryNotReady:
            _LOGGER.debug(
                "Initial refresh failed for %s, continuing setup", battery_name
            )
            await coordinator.async_refresh()

    hass.async_create_task(first_refresh())

    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: SOKConfigEntry) -> bool:
    """Unload a config entry."""
    battery_name = getattr(entry, "title", entry.unique_id)
    _LOGGER.debug("Unloading SOK battery %s", battery_name)
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        coordinator: SOKDataUpdateCoordinator = entry.runtime_data
        await coordinator.async_shutdown()
        entry.runtime_data = None
    return unload_ok


async def async_remove_config_entry_device(
    hass: HomeAssistant, entry: SOKConfigEntry, device_entry: dr.DeviceEntry
) -> bool:
    """Remove a config entry from a device."""
    if any(
        identifier == (DOMAIN, entry.unique_id)
        for identifier in device_entry.identifiers
    ):
        dev_reg = dr.async_get(hass)
        dev_reg.async_remove_device(device_entry.id)
        return True
    return False
