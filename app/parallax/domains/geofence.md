---
title: Geofence
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 10
---

# Geofence (Parallax)

## RVMs

| RVM | Protobuf hints |
| --- | --- |
| `geofence.geofence_service.favoriteGeofences` | `o70/b` (decoder in `cm/c`) |

Favorite geofences list for charging / smart features in the app.

## Legacy

No direct equivalent on [`GetVehicleState`](/app/legacy/vehicle-state). Geofence management is Parallax-first in the home subscription bundle.

Capture payloads and decode with [Decoding](/app/parallax/decoding) workflow.
