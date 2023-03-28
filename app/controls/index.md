---
title: Vehicle Controls
has_children: true
nav_order: 2
---

# App API

## Overview

This section contains endpoints for controlling your vehicle. There are endpoints for locking and unlocking your vehicle, sharing a location to your vehicle, toggling Gear Guard, opening the tailgate/liftgate, and more.

## Enrollment
Vehicle commands require your device to be enrolled as a phone key. You can enroll up to 2 devices at a time. Enrolling a device requires sending a public key and the name for the device - see the [EnrollPhone](/app/controls/enroll-phone) endpoint for more information.


## Endpoints

- [`EnrollPhone`](/app/controls/enroll-phone) - enroll a new phone key
-  [`DisenrollPhone`](/app/controls/disenroll-phone) - disenroll a phone key
- [`ParseAndShareLocationToVehicle`](/app/controls/share-location) - share a location to your vehicle