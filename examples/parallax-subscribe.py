#!/usr/bin/env python3
"""
Minimal ParallaxMessages WebSocket subscriber for the Rivian mobile app.

Requires: pip install websockets

Environment:
  RIVIAN_A_SESS   App session token (a-sess)
  RIVIAN_U_SESS   User session token (u-sess)
  RIVIAN_CSRF     CSRF token
  RIVIAN_VEHICLE_ID  Vehicle id, e.g. 01-123456789

Optional:
  RIVIAN_WS_URL   Defaults to wss://api.rivian.com/gql-consumer-subscriptions/graphql
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import uuid

try:
    import websockets
except ImportError:
    print("Install dependency: pip install websockets", file=sys.stderr)
    raise

WS_URL = os.environ.get(
    "RIVIAN_WS_URL",
    "wss://api.rivian.com/gql-consumer-subscriptions/graphql",
)

# App-scoped RVMs the 3.13.1 consumer app always includes (non-vehicle-state topics).
# See app/parallax/subscription.md for the full list and feature-gated RVMs.
DEFAULT_RVMS = [
    "energy_edge_compute.graphs.parked_energy_distributions",
    "energy_edge_compute.graphs.charging_graph_global",
    "energy_edge_compute.graphs.charge_session_breakdown",
    "energy_edge_compute.graphs.cold_weather_soc",
    "geofence.geofence_service.favoriteGeofences",
    "ota.user_schedule.ota_config",
    "ota.ota_state.vehicle_ota_state",
    "gearguard_streaming.privacy.gearguard_streaming_in_vehicle_consent",
    "gearguard_streaming.privacy.gearguard_streaming_daily_limit",
    "vehicle.wheels.vehicle_wheels",
    "navigation.navigation_service.trip_info",
    "navigation.navigation_service.trip_progress",
    "comfort.cabin.climate_hold_setting",
    "comfort.cabin.cabin_ventilation_setting",
    "comfort.cabin.climate_hold_status",
    "vehicle_access.passive_entry.passive_entry",
    "charging.schedule.time_window",
    "vehicle_access.state.passive_entry",
    "device_table.vas_keyper.devices",
    "body.trailer.state",
    "body.closures.states",
    "body.windows.states",
    "dynamics.vehicle.gnss",
    "dynamics.vehicle.location",
    "dynamics.vehicle.odometer",
    "energy.high_voltage.battery_state",
    "energy.high_voltage.battery_characteristics",
    "charging.session.notification",
    "charging.session.soc_slider",
    "charging.session.trip_target",
    "energy.low_voltage.battery_state",
    "security.alarm.state",
    "security.access.immobilizer_state",
    "security.access.passive_entry_debug",
    "security.access.vas_fault",
    "comfort.user_modes.state",
    "comfort.cabin.cabin_preconditioning_status",
    "comfort.cabin.cabin_temperatures",
    "comfort.cabin.defrost_defog_status",
    "vehicle.power.state",
    "ota.deployment.state",
    "vehicle.network.state",
]

SUBSCRIPTION_QUERY = """
subscription ParallaxMessages($vehicleId: String!, $rvms: [String!]) {
  parallaxMessages(vehicleId: $vehicleId, rvms: $rvms) {
    payload
    timestamp
    rvm
  }
}
""".strip()


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"Missing environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


async def main() -> None:
    a_sess = require_env("RIVIAN_A_SESS")
    u_sess = require_env("RIVIAN_U_SESS")
    csrf = require_env("RIVIAN_CSRF")
    vehicle_id = require_env("RIVIAN_VEHICLE_ID")

    headers = {
        "a-sess": a_sess,
        "u-sess": u_sess,
        "csrf-token": csrf,
        "apollographql-client-name": "com.rivian.android.consumer",
    }

    sub_id = str(uuid.uuid4())

    async with websockets.connect(WS_URL, additional_headers=headers) as ws:
        await ws.send(json.dumps({"type": "connection_init"}))
        while True:
            raw = await ws.recv()
            msg = json.loads(raw)
            if msg.get("type") == "connection_ack":
                break
            if msg.get("type") == "connection_error":
                raise RuntimeError(f"connection_error: {msg}")

        await ws.send(
            json.dumps(
                {
                    "type": "subscribe",
                    "id": sub_id,
                    "payload": {
                        "operationName": "ParallaxMessages",
                        "variables": {
                            "vehicleId": vehicle_id,
                            "rvms": DEFAULT_RVMS,
                        },
                        "query": SUBSCRIPTION_QUERY,
                    },
                }
            )
        )
        print(f"Subscribed to {len(DEFAULT_RVMS)} RVMs for {vehicle_id}", flush=True)

        async for raw in ws:
            msg = json.loads(raw)
            if msg.get("id") != sub_id:
                continue
            kind = msg.get("type")
            if kind == "next":
                px = msg["payload"]["data"]["parallaxMessages"]
                print(
                    json.dumps(
                        {
                            "rvm": px["rvm"],
                            "timestamp": px["timestamp"],
                            "payload_b64": px["payload"],
                        }
                    ),
                    flush=True,
                )
            elif kind == "complete":
                print("subscription complete", flush=True)
                break
            elif kind == "error":
                print(f"subscription error: {msg}", file=sys.stderr, flush=True)
                break


if __name__ == "__main__":
    asyncio.run(main())
