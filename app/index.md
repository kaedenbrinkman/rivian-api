---
title: App API
has_children: true
nav_order: 2
---

# App API

## Overview

This section documents the Rivian Mobile App API. The API is used by the official app to communicate with vehicles: live telemetry, remote commands, charging, account data, and more.

Main GraphQL HTTP endpoints:

- `https://rivian.com/api/gql/orders/graphql` — orders, gear shop
- `https://rivian.com/api/gql/gateway/graphql` — vehicle info, legacy controls, Parallax mutations
- `https://rivian.com/api/gql/chrg/user/graphql` — wallbox, public charging, session history
- `https://rivian.com/api/gql/t2d/graphql` — payments

Live data also uses WebSocket:

- `wss://api.rivian.com/gql-consumer-subscriptions/graphql` — [Parallax](/app/parallax) protobuf streams and [legacy JSON subscriptions](/app/legacy/websocket-subscriptions)

## Authentication

See [Authentication](/app/authentication).

## Getting started

Once authenticated, use [`getUserInfo`](/app/account/user-info/) for your user ID and vehicle IDs.

## Documentation

- [**Parallax**](/app/parallax) — live protobuf vehicle streams by domain, decoding notes, and `sendParallaxPayload` commands
- [**Feature flags**](/app/feature-flags) — Firebase app remote config + per-vehicle `SupportedFeatures` gating (including Parallax)
- [**Legacy**](/app/legacy) — typed JSON `GetVehicleState`, HMAC `sendVehicleCommand`, wallbox/charging HTTP, and non-Parallax WebSocket subscriptions
- [**Account**](/app/account) — orders, payment methods, linked products, personal info
- [**Gear Shop**](/app/gear-shop) — product details and pricing
