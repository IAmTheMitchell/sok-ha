"""Config flow for sok ble integration."""

from __future__ import annotations

from typing import Any

import voluptuous as vol
from homeassistant.components.bluetooth import BluetoothServiceInfoBleak

try:  # Home Assistant 2025.3+
    from homeassistant.components.bluetooth import async_discovered_service_info
    _ASYNC_DISCOVERY = "service_info"
except ImportError:  # pragma: no cover - older Home Assistant versions
    from homeassistant.components.bluetooth import async_scanner_devices_by_address
    _ASYNC_DISCOVERY = "device"
from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_ADDRESS

from .const import DOMAIN


class SOKConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for sok."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""
        self._discovery_info: BluetoothServiceInfoBleak | None = None
        self._discovered_devices: dict[str, str] = {}

    @staticmethod
    def _device_supported(discovery_info: BluetoothServiceInfoBleak) -> bool:
        """Return True if the discovered device looks like a SOK battery."""
        name = discovery_info.name or ""
        return name.startswith("SOK")

    async def async_step_bluetooth(
        self, discovery_info: BluetoothServiceInfoBleak
    ) -> ConfigFlowResult:
        """Handle the bluetooth discovery step."""
        await self.async_set_unique_id(discovery_info.address)
        self._abort_if_unique_id_configured()
        if not self._device_supported(discovery_info):
            return self.async_abort(reason="not_supported")
        self._discovery_info = discovery_info
        return await self.async_step_bluetooth_confirm()

    async def async_step_bluetooth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Confirm discovery."""
        assert self._discovery_info is not None
        discovery_info = self._discovery_info
        title = discovery_info.name or discovery_info.address
        if user_input is not None:
            return self.async_create_entry(title=title, data={})

        self._set_confirm_only()
        placeholders = {"name": title}
        self.context["title_placeholders"] = placeholders
        return self.async_show_form(
            step_id="bluetooth_confirm", description_placeholders=placeholders
        )

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the user step to pick discovered device."""
        if user_input is not None:
            address = user_input[CONF_ADDRESS]
            await self.async_set_unique_id(address, raise_on_progress=False)
            self._abort_if_unique_id_configured()
            title = self._discovered_devices[address]
            return self.async_create_entry(title=title, data={})

        current_addresses = self._async_current_ids(include_ignore=False)
        if _ASYNC_DISCOVERY == "service_info":
            discoveries = async_discovered_service_info(self.hass, False)
        else:
            discoveries = async_scanner_devices_by_address(self.hass).values()
        for discovery_info in discoveries:
            address = discovery_info.address
            if address in current_addresses or address in self._discovered_devices:
                continue
            if self._device_supported(discovery_info):
                self._discovered_devices[address] = (
                    discovery_info.name or address
                )

        if not self._discovered_devices:
            return self.async_abort(reason="no_devices_found")

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {vol.Required(CONF_ADDRESS): vol.In(self._discovered_devices)}
            ),
        )
