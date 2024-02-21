---
title: Vehicle Info Endpoints
has_children: true
parent: App API
nav_order: 3
permalink: /app/vehicle-info
---

# Vehicle Info Endpoints

## Overview

These endpoints return information about the vehicle.

## Endpoints

- [`Subscriptions`](/app/vehicle-info/subscriptions) - subscribe to vehicle state (e.g. location, speed, tire pressure, etc.) over a websocket connection
- [`RegisterPushNotificationToken`](/app/vehicle-info/push-notifications) - register a push notification token for your account
- [`getOTAUpdateDetails`](/app/vehicle-info/ota-update-details) - get OTA update details (release notes)
- [`getVehicleImages`](/app/vehicle-info/vehicle-images) - get images for your vehicle configuration
- [`GetVehicleLastConnection`](/app/vehicle-info/vehicle-last-connection) - get the last time your vehicle synced to Rivian Cloud
- [`GetVehicleState`](/app/vehicle-info/vehicle-state) - get vehicle state information
- [`GetVehicle`](/app/vehicle-info/vehicle) - get information about vehicle keys and drivers
- [`SetVehicleName`](/app/vehicle-info/set-vehicle-name) - set your vehicle name
- [`SupportedFeatures`](/app/vehicle-info/supported-features) - get feature flags enabled for all vehicles in your account
- [`FileWrapper`](/app/vehicle-info/file-wrapper) - get documents such as the R1T and R1S owners guides
