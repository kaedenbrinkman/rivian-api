---
title: Enroll a Phone Key
parent: BLE API
has_children: false
nav_order: 3
---

# Enroll a Phone Key
Phone Key enrollment is done over a web API endpoint. See [EnrollPhone](/app/enroll-phone) for details.

Once enrolled, the phone is authorized to pair with the `Rivian Phone Key` peripheral. The phone will then be able to send commands to the vehicle, with each command including a HMAC just like the [`sendVehicleCommand`](/app/controls/send-vehicle-command) endpoint.