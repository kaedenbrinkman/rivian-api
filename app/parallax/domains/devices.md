---
title: Devices
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 13
---

# Devices (Parallax)

Phone keys and VAS keyper device table.

## RVMs

| RVM | Notes |
| --- | --- |
| `device_table.vas_keyper.devices` | Enrolled phone keys / VAS devices visible to vehicle |

Protobuf parsed in `cm/c` (wheel/device-adjacent structures in `q70/*` family).

## Legacy

- [`EnrollPhone`](/app/legacy/controls/enroll-phone) / [`DisenrollPhone`](/app/legacy/controls/disenroll-phone) — register keys (HTTP + HMAC).
- [`GetVehicle`](/app/legacy/vehicle-info/vehicle) — drivers and keys metadata.

Parallax RVM streams live device table state to the vehicle; enrollment remains legacy HTTP.
