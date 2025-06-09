from types import SimpleNamespace

from custom_components.sok.sensor import SENSOR_DESCRIPTIONS

class DummyCoordinator:
    def __init__(self, device):
        self.data = device
        self.address = "00:11:22:33:44:55"

def test_sensor_descriptions_value():
    device = SimpleNamespace(
        voltage=12.5,
        current=5.0,
        soc=80,
        temperature=25.0,
        capacity=100.0,
        num_cycles=10,
        power=62.5,
    )
    coordinator = DummyCoordinator(device)

    for desc in SENSOR_DESCRIPTIONS:
        # Each sensor description should return a value without error
        assert desc.value_fn(device) is not None
