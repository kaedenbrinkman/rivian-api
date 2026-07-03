---
title: Decoding
parent: Parallax
grand_parent: App API
has_children: false
nav_order: 2
---

# Decoding Parallax payloads

## Pipeline

1. Base64-decode `payload`.
2. Parse bytes as protobuf (schema depends on `rvm`).
3. Optionally correlate with [Legacy `GetVehicleState`](/app/legacy/vehicle-state) JSON for field names and units.

No public `.proto` files exist. Recover schemas from decompiled generated classes (`k70`, `l70`, `g70`, `f70`, `n70`, …).

## Quick inspection

```bash
echo '<payload-b64>' | base64 -d | protoc --decode_raw
```

## APK decode entry points

| File | Role |
| --- | --- |
| `cm/c.smali` | RVM enum + `parseRvmData()` for most topics |
| `cq/f.smali` | Extra decoders (`charging.session.status` → `f70/v`, `energy.high_voltage.battery_state` → `l70/p`, …) |
| `cm/b.smali` | Enum → handler mapping |

## Money submessages

Session cost and similar fields use `tk/b`:

| Field | Type |
| --- | --- |
| `currencyCode` | string (e.g. `USD`) |
| `units` | int64 major units |
| `nanos` | int32 fractional nanos |

## Workflow for building `.proto` files

1. Read `FIELD_NUMBER` lines from the APK class for that RVM.
2. Capture samples via [subscription script](../../examples/parallax-subscribe.py) or MITM.
3. Validate with `protoc --decode_raw` and domain pages under [Domains](/app/parallax/domains).
4. Snapshot [GetVehicleState](/app/legacy/vehicle-state) at the same time to label enums and floats.

Domain pages document known message types per RVM.
