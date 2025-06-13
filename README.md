# SOK BLE Integration for Home Assistant

This custom integration polls data from SOK batteries using Bluetooth Low Energy (BLE).
It has been tested with SK12V100H batteries and should work with other SOK models
that advertise as `SOK-AA`.

## Features
- Automatic discovery of SOK batteries
- Battery monitoring sensors
  - Voltage
  - Current
  - Power
  - State of charge
  - Temperature
  - Capacity
  - Charge cycles
  - Cell voltages (1-4)
- Energy In and Energy Out sensors for the Energy Dashboard
- Polling interval of three minutes
- Automatic error recovery on connection issues

## Prerequisites
- Home Assistant 2025.3 or newer
- SOK battery with BLE module (tested with SK12V100H)
- Bluetooth adapter available to Home Assistant

## Installation
Install via [HACS](https://hacs.xyz/):
1. Ensure HACS is installed
2. Add this repository as a custom repository in HACS
3. Search for "SOK" and install the integration
4. Restart Home Assistant

## Configuration
After installation:
1. Go to **Settings > Devices & Services**
2. Click **+ Add Integration** and choose **SOK**
3. Follow the prompts to select your battery

## Troubleshooting
- Ensure the battery is powered on and in Bluetooth range
- Enable debug logging for the integration when reporting issues

## License
This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.
