---
title: getVehicleWheelImages
parent: Vehicle Info Endpoints
grand_parent: App API
has_children: false
nav_order: 3
---

# getVehicleWheelImages

## Overview

The `getVehicleWheelImages` url returns a wheel image for your wheel id.

### Example Request

Make a GET request to:
```
https://rivian.com/mobile/static/img/v1/features/wheels/<your wheel option>.png
```

`<your wheel option> can be found in the CurrentUserForLogin response as wheelOption.optionId`

An example option ID is `WHL-0AS`

### Example Response

![Wheel WHL-0A1](https://rivian.com/mobile/static/img/v1/features/wheels/WHL-0AS.png)
