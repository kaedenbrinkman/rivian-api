---
title: OTA
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 8
---

# OTA (Parallax)

Over-the-air update schedule, download state, deployment.

## RVMs

| RVM | Protobuf hints | Legacy correlate |
| --- | --- | --- |
| `ota.user_schedule.ota_config` | `r70/u`, `r70/i` | `otaInstallTime`, schedule |
| `ota.ota_state.vehicle_ota_state` | | `otaStatus`, `otaCurrentStatus`, download/install progress |
| `ota.deployment.state` | | `otaInstallReady`, version fields |

Legacy query [`getOTAUpdateDetails`](/app/legacy/vehicle-info/ota-update-details) — release notes (HTTP, not Parallax).

## Commands

Install-now → `PARALLAX_OTA_COMMAND` + [sendParallaxPayload](/app/parallax/commands/send-payload).

## Legacy JSON

Most OTA progress fields still appear on [`GetVehicleState`](/app/legacy/vehicle-state) and `vehicleState` WebSocket subscription.
