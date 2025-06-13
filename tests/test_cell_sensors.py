from types import SimpleNamespace
from custom_components.sok_battery.sensor import SENSOR_DESCRIPTIONS


def test_cell_sensor_values():
    device = SimpleNamespace(cell_voltages=[3.1, 3.2, 3.3, 3.4])
    values = {
        desc.key: desc.value_fn(device)
        for desc in SENSOR_DESCRIPTIONS
        if desc.key.startswith("cell_")
    }
    assert values["cell_1_voltage"] == 3.1
    assert values["cell_2_voltage"] == 3.2
    assert values["cell_3_voltage"] == 3.3
    assert values["cell_4_voltage"] == 3.4
