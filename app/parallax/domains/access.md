---
title: Access
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 7
---

# Access (Parallax)

Passive entry configuration and state.

## RVMs

| RVM | Notes |
| --- | --- |
| `vehicle_access.passive_entry.passive_entry` | Passive entry setting |
| `vehicle_access.state.passive_entry` | Passive entry runtime state |

Related security RVMs: `security.access.passive_entry_debug`, `security.access.btm`, `security.access.vas_fault` — see [Security](/app/parallax/domains/security).

## Legacy

Phone key enrollment affects access but uses [Legacy controls](/app/legacy/controls) (`EnrollPhone` / `DisenrollPhone`), not Parallax RVMs.

## Devices

Enrolled phone keys listed under [Devices](/app/parallax/domains/devices) (`device_table.vas_keyper.devices`).
