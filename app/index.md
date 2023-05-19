---
title: App API
has_children: true
nav_order: 2
---

# App API

## Overview

This section contains endpoints from the official Rivian Mobile App API. The API is used by the Rivian Mobile App to communicate with the vehicle. Using the API, you can get information about the vehicle, send commands to the vehicle, and receive notifications from the vehicle.

There are four main GraphQL endpoints:
- `https://rivian.com/api/gql/orders/graphql` (orders, gear shop, etc.)
- `https://rivian.com/api/gql/gateway/graphql` (vehicle info, controls, etc.)
- `https://rivian.com/api/gql/chrg/user/graphql` (charging)
- `https://rivian.com/api/gql/t2d/graphql` (payments)

## Authentication

See [Authentication](/app/authentication) for more information.

## Getting started

Once authenticated, check out the [`getUserInfo`](/app/account/user-info/) endpoint to get your user ID and vehicle ID. You can use these IDs to make requests to the API.

## What can you do?

- [`Account Information`](/app/account): view your orders, connected accounts, payment methods, linked products, and personal info.
- [`Charging`](/app/charging): view the status of your wallbox and charging sessions.
- [`Controls`](/app/controls): lock/unlock your vehicle, share a location to your vehicle, plan a trip, and more.
- [`Vehicle Information`](/app/vehicle-info): view your vehicle's VIN, state of charge, odometer, location, OTA update release notes, and more.
- [`Gear Shop`](/app/gear-shop): view product details and their pricing