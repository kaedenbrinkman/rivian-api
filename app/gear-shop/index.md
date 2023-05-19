---
title: Gear Shop Endpoints
has_children: true
parent: App API
nav_order: 3
permalink: /app/gear-shop
---

# Gear Shop Endpoints

## Overview

These endpoints return information about items in the Rivian Gear Shop. They do not require authentication, but they do require a valid `csrf-token` and `dc-cid` correlation ID.

## Endpoints

- [`SearchShopProductsBySkus`](/app/gear-shop/search-items) - search items
- [`SearchShopPricingBySku`](/app/gear-shop/pricing) - get pricing for items