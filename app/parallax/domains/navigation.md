---
title: Navigation
parent: Domains
grand_parent: Parallax
great_grand_parent: App API
has_children: false
nav_order: 9
---

# Navigation (Parallax)

Active trip routing from the vehicle navigation service.

## RVMs

| RVM | Protobuf | Notes |
| --- | --- | --- |
| `navigation.navigation_service.trip_info` | `t70/v` | Trip metadata, legs, stops, polyline, ETAs |
| `navigation.navigation_service.trip_progress` | `t70/x` | Progress along active trip |

Decoders in `cm/c.parseRvmData()` — nested repeated fields for legs, stops, coordinates, EV charge filters.

## Legacy

Trip **planning** (not live progress) uses HTTP [`planTrip`](/app/legacy/vehicle-info/plan-trip).

Share destination to vehicle: [ParseAndShareLocationToVehicle](/app/legacy/controls/share-location).

## Decoding tips

Trip payloads are large multi-message protos. Use `protoc --decode_raw` on captured samples; field  lists include `getLegsList`, `getStopsList`, `getPolyline`, `getTripEtaUTC` in smali accessor names.
