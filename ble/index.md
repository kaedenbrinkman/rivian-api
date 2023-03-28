---
title: BLE API
has_children: true
nav_order: 2
---

# BLE API

## Overview

This section contains information about the Rivian Phone Key BLE API. The API is used by the Rivian Phone Key to communicate directly with the vehicle, without an internet connection.

These commands mirror the internet-based commands in the [`sendVehicleCommand`](/app/controls/send-vehicle-command) endpoint. The BLE API allows for commands to be sent quicker when you are near your vehicle. BLE is also used for proximity detection, both for phone key and the key fob.

# BLE Devices

- Rivian Sensor 1 For sensing the proximity of BLE keys
- Rivian Sensor 2: For sensing the proximity of BLE keys
- Rivian Sensor 3: For sensing the proximity of BLE keys
- Rivian Sensor 4: For sensing the proximity of BLE keys
- RIVN: Unknown
- Rivian Phone Key: For communicating with the vehicle to perform commands
- Rivian Audio: For playing music / taking calls in the vehicle
- Rivian Camp Speaker: For playing music / taking calls on the camp speaker

The BLE API uses the "Rivian Phone Key" device to send VAS commands and receive data. The device has the following characteristics:

- `52495356-454e-534f-5253-455256494345`: Service UUID (Active Entry)
- `5249565f-4d4f-424b-4559-5f5752495445`: Characteristic UUID (Read/Write, Active Entry)
- `5ae32b92-eafb-471b-afe8-e88eec4a4774`: Characteristic UUID (Unknown)
- `afb2e704-842b-4e6a-9bd2-b1b305828f24`: Characteristic UUID (Read, Vehicle Status)

## List of Commands

```
WAKE_VEHICLE
OPEN_FRUNK
CLOSE_FRUNK
OPEN_ALL_WINDOWS
CLOSE_ALL_WINDOWS
UNLOCK_ALL_CLOSURES
LOCK_ALL_CLOSURES
ENABLE_GEAR_GUARD_VIDEO
DISABLE_GEAR_GUARD_VIDEO
HONK_AND_FLASH_LIGHTS
OPEN_TONNEAU_COVER
CLOSE_TONNEAU_COVER
```
