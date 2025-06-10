"""Support for SOK BLE sensors."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable
import logging

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfPower,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import (
    CONNECTION_BLUETOOTH,
    DeviceInfo,
)
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

_LOGGER = logging.getLogger(__name__)
from sok_ble.sok_bluetooth_device import SokBluetoothDevice

from . import SOKConfigEntry
from .const import DOMAIN


@dataclass
class SokSensorEntityDescription(SensorEntityDescription):
    """Describe a SOK sensor."""

    value_fn: Callable[[SokBluetoothDevice], int | float | None] | None = None


SENSOR_DESCRIPTIONS: tuple[SokSensorEntityDescription, ...] = (
    SokSensorEntityDescription(
        key="voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.voltage,
    ),
    SokSensorEntityDescription(
        key="current",
        device_class=SensorDeviceClass.CURRENT,
        native_unit_of_measurement=UnitOfElectricCurrent.AMPERE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.current,
    ),
    SokSensorEntityDescription(
        key="power",
        device_class=SensorDeviceClass.POWER,
        native_unit_of_measurement=UnitOfPower.WATT,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.power,
    ),
    SokSensorEntityDescription(
        key="soc",
        device_class=SensorDeviceClass.BATTERY,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.soc,
    ),
    SokSensorEntityDescription(
        key="temperature",
        device_class=SensorDeviceClass.TEMPERATURE,
        native_unit_of_measurement=UnitOfTemperature.CELSIUS,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.temperature,
    ),
    SokSensorEntityDescription(
        key="capacity",
        name="Capacity",
        icon="mdi:battery-high",
        native_unit_of_measurement="Ah",
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.capacity,
    ),
    SokSensorEntityDescription(
        key="num_cycles",
        name="Charge Cycles",
        icon="mdi:battery-sync",
        native_unit_of_measurement="cycles",
        state_class=SensorStateClass.TOTAL_INCREASING,
        value_fn=lambda dev: dev.num_cycles,
    ),
    SokSensorEntityDescription(
        key="cell_1_voltage",
        name="Cell 1 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.cell_voltages[0] if dev.cell_voltages else None,
    ),
    SokSensorEntityDescription(
        key="cell_2_voltage",
        name="Cell 2 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.cell_voltages[1] if dev.cell_voltages else None,
    ),
    SokSensorEntityDescription(
        key="cell_3_voltage",
        name="Cell 3 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.cell_voltages[2] if dev.cell_voltages else None,
    ),
    SokSensorEntityDescription(
        key="cell_4_voltage",
        name="Cell 4 Voltage",
        device_class=SensorDeviceClass.VOLTAGE,
        native_unit_of_measurement=UnitOfElectricPotential.VOLT,
        state_class=SensorStateClass.MEASUREMENT,
        value_fn=lambda dev: dev.cell_voltages[3] if dev.cell_voltages else None,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: SOKConfigEntry,
    async_add_entities: AddConfigEntryEntitiesCallback,
) -> None:
    """Set up the SOK BLE sensors."""
    coordinator = entry.runtime_data
    entities: list[SOKSensorEntity] = [
        SOKSensorEntity(coordinator, description) for description in SENSOR_DESCRIPTIONS
    ]
    async_add_entities(entities)


class SOKSensorEntity(CoordinatorEntity[SokBluetoothDevice], SensorEntity):
    """Representation of a SOK BLE sensor."""

    entity_description: SokSensorEntityDescription

    def __init__(self, coordinator, description: SokSensorEntityDescription) -> None:
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{coordinator.address}_{description.key}"
        self._attr_has_entity_name = True
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, coordinator.unique_id)},
            connections={(CONNECTION_BLUETOOTH, coordinator.address)},
            name=getattr(coordinator.entry, "title", coordinator.address),
            manufacturer="SOK",
        )

    @property
    def native_value(self) -> int | float | None:
        """Return the sensor value."""
        device: SokBluetoothDevice | None = self.coordinator.data
        if device is None:
            return None
        if description := self.entity_description.value_fn:
            try:
                return description(device)
            except AttributeError as err:  # pragma: no cover - defensive
                _LOGGER.debug("Missing attribute for %s: %s", self.unique_id, err)
        return None
