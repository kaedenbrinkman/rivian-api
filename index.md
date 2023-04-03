---
title: Home
nav_order: 1
---

# Unofficial Rivian API Documentation

<div style="border: 1px solid #ffc107; background-color: #fff3cd; color: #856404; padding: 1em;">
  <p><strong>WARNING:</strong> This information is not maintained by Rivian, and things could change or break at any moment. Use at your own risk.</p>
</div>

Most Rivian web APIs use GraphQL. Learn more about GraphQL [here](https://graphql.org/).

## App API
This section contains information about the endpoints that the Rivian mobile app uses to fetch information about your vehicle or account. It also supports some controls, such as locking/unlocking, etc. See [App API](/app) for more information.

## Vehicle BLE API
The BLE API is used by the mobile app and keyfob. It supports the same controls found in the app API, but sends the commands directly to the vehicle over BLE instead of over the internet. See [Vehicle BLE API](/ble) for more information.

## Vehicle CAN API
Inside the car, components communicate with one another on a CAN network. By listening to them, you can collect detailed information about the vehicle. R1 vehicles have a lot of separate CAN busses. See [Vehicle CAN API](/can) for more information.

## Configurator Image API
The official website has an API for displaying images of different R1 configurations. See [Configurator API](/configurator/) for more information.

## Hardware Teardown
Interested in repairing your vehicle? This is a page for resources and tips. See [Hardware Teardown](/teardown/) for more information.

## Contributing
To contribute, submit a pull request to the [GitHub repository](https://github.com/kaedenbrinkman/rivian-api).