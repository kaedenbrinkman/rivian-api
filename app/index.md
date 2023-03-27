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

- [`delivery`](/app/deliveries) - get delivery information for an order
- [`EnrollPhone`](/app/enroll-phone) - enroll a new phone key
- [`getNonRivianUserSession`](/app/non-rivian-user-session) - get non-Rivian charging session details
- [`vehicleOrders`](/app/vehicle-orders) - list vehicle orders for your account
- [`searchOrders`](/app/searchOrders) - list retail orders for your account
- [`order`](/app/order) - get order details
- [`transactionStatus`](/app/transaction-status) - get transaction details (steps)
- [`financeSummary`](/app/finance-summary) - get financing details
- [`planTrip`](/app/plan-trip) - plan charging for a trip
- [`GetProvisionedCampSpeakers`](/app/provisioned-camp-speakers) - list camp speakers in your account
- [`RegisterPushNotificationToken`](/app/push-notifications) - register a push notification token for your account
- [`getRegisteredWallboxes`](/app/registered-wallboxes) - list Rivian Chargers in your account
- [`ParseAndShareLocationToVehicle`](/app/share-location) - share a location to your vehicle
- [`getUserInfo`](/app/user-info) - get user information
- [`user`](/app/user) - get user information for orders
- [`paymentMethods`](/app/payment-methods) - get user payment methods
- [`CheckByRivianId`](/app/check-by-rivian-id) - shows third-party accounts linked to your Rivian account
- [`getLinkedEmailForRivianId`](/app/get-linked-email-for-rivian-id) - shows email addresses for third-party accounts linked to your Rivian account
- [`getOTAUpdateDetails`](/app/ota-update-details) - get OTA update details (release notes)
- [`getVehicleImages`](/app/vehicle-images) - get images for your vehicle configuration
- [`GetVehicleLastConnection`](/app/vehicle-last-connection) - get the last time your vehicle synced to Rivian Cloud
- [`GetVehicleState`](/app/vehicle-state) - get vehicle state information
- [`GetVehicle`](/app/vehicle) - get information about vehicle keys and drivers

The app calls `GetVehicleState` every 1000ms.
