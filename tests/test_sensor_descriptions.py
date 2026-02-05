from types import SimpleNamespace
from typing import cast

from sok_ble.sok_bluetooth_device import SokBluetoothDevice

from custom_components.sok_battery.sensor import SENSOR_DESCRIPTIONS


class DummyCoordinator:
    def __init__(self, device):
        self.data = device
        self.address = "00:11:22:33:44:55"


def test_sensor_descriptions_value():
    device = cast(
        SokBluetoothDevice,
        SimpleNamespace(
            voltage=12.5,
            current=5.0,
            soc=80,
            temperature=25.0,
            capacity=100.0,
            num_cycles=10,
            power=62.5,
            cell_voltages=[3.3, 3.3, 3.3, 3.3],
        ),
    )
    DummyCoordinator(device)

    for desc in SENSOR_DESCRIPTIONS:
        # Each sensor description should return a value without error
        if desc.value_fn is not None:
            assert desc.value_fn(device) is not None


def test_voltage_sensor_precision():
    voltage_keys = {
        "voltage",
        "cell_1_voltage",
        "cell_2_voltage",
        "cell_3_voltage",
        "cell_4_voltage",
    }

    for desc in SENSOR_DESCRIPTIONS:
        if desc.key in voltage_keys:
            assert desc.suggested_display_precision == 2
