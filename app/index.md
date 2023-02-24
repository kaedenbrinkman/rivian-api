---
title: App API
has_children: true
nav_order: 2
---

# App API

## Overview
This section contains endpoints from the official Rivian Mobile App API. The API is used by the Rivian Mobile App to communicate with the vehicle. Using the API, you can get information about the vehicle, send commands to the vehicle, and receive notifications from the vehicle.

## Authentication
See [Authentication](/app/authentication) for more information.


## Endpoints
- `delivery` - get delivery information for an order
- `EnrollPhone` - enroll a new phone key
- `getNonRivianUserSession` - get non-Rivian charging session details
- `vehicleOrders` - list vehicle orders for your account
- `searchOrders` - list retail orders for your account
- `order` - get order details
- `planTrip` - plan charging for a trip
- `GetProvisionedCampSpeakers` - list camp speakers in your account
- `RegisterPushNotificationToken` - register a push notification token for your account
- `getRegisteredWallboxes` - list Rivian Chargers in your account
- `ParseAndShareLocationToVehicle` - share a location to your vehicle
- `getUserInfo` - get user information
- `user` - get user information for orders
- `getVehicleImages` - get images for your vehicle configuration
- `GetVehicleLastConnection` - get the last time your vehicle synced to Rivian Cloud
- `GetVehicleState` - get vehicle state information
- `GetVehicle` - get information about vehicle keys and drivers



The app calls `GetVehicleState` every 1000ms.