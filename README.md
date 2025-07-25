![CI](https://github.com/IAmTheMitchell/sok-ha/actions/workflows/ci.yml/badge.svg)
![Hassfest](https://github.com/IAmTheMitchell/sok-ha/actions/workflows/hassfest.yml/badge.svg)
![HACS](https://github.com/IAmTheMitchell/sok-ha/actions/workflows/validate.yml/badge.svg)

# SOK BLE Integration for Home Assistant

This custom integration polls data from SOK batteries using Bluetooth Low Energy (BLE).

![Example dashboard using data from the integration.](docs/images/dashboard.png)

## Currently Supported Devices
Tested:
- SK12V100H

Should work, but untested:
- SK12V100P
- SK12V206H
- SK12V206PH
- SK12V280H
- SK24V100
- Any other SOK models that advertise as `SOK-AA` and use the V8 SOK BMS.

(Please open a GitHub issue with your results if you test any of the untested battery models.)

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
- SOK battery with BLE module compatible with the ABC-BMS app (tested with SK12V100H)
- Bluetooth radio available to Home Assistant (built-in radios may or may not work)

## Hardware
_Includes Amazon affiliate links which provide a small commission to support this project._
- Supported [SOK Battery](https://amzn.to/44JXK6r) with Bluetooth BMS
- Bluetooth radio for Home Assistant
  - [ESP32 for Bluetooth proxy](https://amzn.to/4lSBHkV) (Recommended)
  - [USB Bluetooth adapter](https://amzn.to/4lsxDrU)


## Installation
[Installation walkthrough video](https://youtu.be/vmIwiQ0O7yM?si=UDCQHbHkgCKsjNgM)

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
Infrequent disconnects are expected. The integration should recover in the next scanning interval. If data is missing for long periods of time or the integration fails to intialize, try these steps:
- Ensure the battery is in Bluetooth range
- Ensure the battery is charged and not in storage mode
- Enable debug logging for the integration when reporting issues
- Try connecting to the battery using a phone or tablet and the ABC-BMS app

## Support
- For bugs, please open an issue on GitHub
- Include Home Assistant logs and your device model information

## License
This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.
