---
title: Vehicle info
has_children: true
parent: Legacy
grand_parent: App API
nav_order: 4
permalink: /app/legacy/vehicle-info
---

# Legacy vehicle info

HTTP queries for account/vehicle metadata, trip planning, OTA release notes, and static assets. Live state is preferentially streamed via [Parallax](/app/parallax).

## Endpoints

- [`VehiclesAndEnrollments`](/app/legacy/vehicle-info/vehicles-and-enrollments) - list vehicles, configuration, and key enrollments
- [`planTrip`](/app/legacy/vehicle-info/plan-trip) - plan charging for a trip
- [`RegisterPushNotificationToken`](/app/legacy/vehicle-info/push-notifications) - register a push notification token for your account
- [`getOTAUpdateDetails`](/app/legacy/vehicle-info/ota-update-details) - get OTA update details (release notes)
- [`getVehicleImages`](/app/legacy/vehicle-info/vehicle-images) - get images for your vehicle configuration
- [`GetVehicleLastConnection`](/app/legacy/vehicle-info/vehicle-last-connection) - get the last time your vehicle synced to Rivian Cloud
- [`GetVehicleState`](/app/legacy/vehicle-state) - get vehicle state as JSON (Parallax also streams much of this)
- [`GetVehicle`](/app/legacy/vehicle-info/vehicle) - get information about vehicle keys and drivers
- [`SetVehicleName`](/app/legacy/vehicle-info/set-vehicle-name) - set your vehicle name
- [`VehicleNames`](/app/legacy/vehicle-info/vehicle-names) - get custom names for all vehicles
- [`SupportedFeatures`](/app/legacy/vehicle-info/supported-features) - get supported app feature flags per vehicle
- [`GetReverseGeocode`](/app/legacy/vehicle-info/reverse-geocode) - convert coordinates to a formatted address
- [`getVehicleTireImages`](/app/legacy/vehicle-info/vehicle-tire-images) - get wheel diagram image for tire pressure UI
