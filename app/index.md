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

## Getting started

Once authenticated, check out the [`getUserInfo`](/app/user-info) endpoint to get your user ID and vehicle ID. You can use these IDs to make requests to the API.

## Endpoints

- [`Account Information`](/app/account/): view your orders, connected accounts, payment methods, linked products, and personal info.
- [`Charging`](/app/charging/): view the status of your wallbox and charging sessions.
- [`Controls`](/app/controls/): lock/unlock your vehicle, share a location to your vehicle, and more.
- [`Vehicle Information`](/app/vehicle-info/): view your vehicle's VIN, state of charge, odometer, location, OTA update release notes, and more.