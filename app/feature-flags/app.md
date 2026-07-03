---
title: App remote config
parent: Feature flags
grand_parent: App API
has_children: false
nav_order: 1
---

# App remote config flags

Firebase Remote Config boolean flags compiled into the app as enum `wy/b`. Each entry has a **Kotlin enum name** and a **Firebase key** (`getFlagName()`).

The app fetches these at startup via `js/d` (`RemoteConfigManager`). Debug builds can override them in the feature-flag editor (`FeatureFlagEditor`).

There is no public GraphQL query for these values — they are client-side Firebase config, not the per-vehicle `SupportedFeatures` list.

## Flag catalog

| Enum | Firebase key | Typical use (from naming / call sites) |
| --- | --- | --- |
| `PHONE_BATTERY_LEVEL_MONITORING` | `phoneBatteryLevelMonitoring` | Monitor phone battery for BLE / key behavior |
| `PHONE_POSITION_MOTION_STATUS` | `phonePositionMotionStatus` | Phone motion / position for passive entry |
| `DELAY_BLE_UPDATES_UNTIL_FOREGROUND` | `delayBLEUpdatesUntilForeground` | Defer BLE state updates until app foreground |
| `SIMULATE_ACTIVE_COMMAND_SUCCESS_FOR_CLOUD` | `simulateActiveCommandSuccessForCloud` | Debug / test cloud command success |
| `CHARGING_PRICING_DETAILS` | `touPricing` | Time-of-use charging price details |
| `TRIP_TARGET` | `tripTarget` | Charging trip target UI |
| `COLD_WEATHER` | `coldWeather` | Cold-weather energy UI |
| `REVISED_INFO_ARCH_NAV` | `revisedInfoArchNav` | Revised navigation info architecture |
| `PARKED_ENERGY_MONITOR` | `parkedLiveEnergyMonitor` | Parked energy monitor cards |
| `ACTIVE_ENERGY_MONITOR` | `activeLiveEnergyMonitor` | Active session energy monitor |
| `SMART_CHARGING` | `smartCharging` | Smart charging features |
| `PARALLAX_COMMAND` | `parallaxCommand` | Route commands through `sendParallaxPayload` |
| `PARALLAX_VEHICLE_STATE` | `parallaxVehicleState` | Prefer Parallax RVMs for vehicle state |
| `BLE_SCAN_LIMIT_HIT_HANDLING` | `bleScanLimitHitHandling` | Handle Android BLE scan limits |
| `LIVE_CHAT_NATIVE` | `liveChatNative` | In-app live chat |
| `SERVICE_AI_CHAT` | `serviceAIChat` | Service AI chat |
| `TRANSFER_TO_LIVE_CHAT` | `transferToLiveChat` | Hand off to live chat |
| `TRANSFER_TO_SUPPORT` | `transferToSupport` | Hand off to support |
| `RIVIAN_INTELLIGENCE` | `rivianIntelligence` | Rivian Assistant / intelligence features |
| `MANUAL_REQUEST_DRAFT_CREATION` | `manualRequestDraftCreation` | Service request draft flow |
| `PREVENT_BLE_SERVICE_FOR_CCC` | `preventBleServiceForCCC` | BLE service restrictions for Car Key |
| `HONK_AND_FLASH` | `honkAndFlash` | Honk-and-flash command UI |
| `TWO_FACTOR_DRIVE` | `twoFactorDrive` | Two-factor drive authorization |
| `VISUAL_LOGS` | `visualLogs` | Visual debug logging |
| `FOR_WHATS_NEW_TEST_DO_NOT_REMOVE` | `forWhatsNewTestDoNotRemove` | Internal what's-new test flag |
| `DELETE_BLE_BOND_FOR_CCC_MIGRATION` | `deleteBleBondForCCC` | CCC migration BLE bond cleanup |
| `AUTONOMY_PLUS` | `autonomyPlus` | Autonomy+ subscription features |
| `ADD_AND_REPLACE_BLE_OPERATIONS` | `addAndReplaceBleOperations` | BLE operation batching |
| `IONNA_NETWORK` | `ionnaNetwork` | Ionna charging network in map / planner |
| `ELECTRIFY_AMERICA_NETWORK` | `electrifyAmericaNetwork` | Electrify America network |
| `ICE_RESTART` | `iceRestart` | Infotainment cold-restart command path |
| `CCC_REGENERATE_OWNER_KEY` | `cccRegenerateOwnerKey` | Regenerate CCC owner key |
| `VEHICLE_CONNECTIVITY_PARALLAX` | `vehicleConnectivityParallax` | Vehicle connectivity over Parallax |
| `VIDEO_DOWNLOADING` | `videoDownloading` | Gear Guard video download (app-side) |
| `BLE_SCAN_PASSIVE` | `bleScanPassive` | Passive BLE scanning mode |
| `ANDROID_CDM_PROMPT` | `androidCdmPrompt` | Android Companion Device Manager prompt |
| `PASSIVE_ENTRY_FAILURE` | `passiveEntryFailure` | Passive entry failure handling UX |
| `VERBOSE_CLOUD_LOGS` | `verboseCloudLogs` | Verbose cloud logging |
| `DEVICE_TABLE_VAS_KEYPER_DEVICES` | `deviceTableVasKeyperDevices` | Phone key device table Parallax RVM |
| `REFRESH_BLUETOOTH_DIALOG` | `refreshBluetoothDialog` | Bluetooth refresh dialog |
| `PROFILE_PIN` | `profilePin` | In-vehicle profile PIN ([User PIN](/app/account/user-pin)) |
| `SCHEDULING_FLOW_TRANSFER_TO_LIVE_CHAT` | `schedulingFlowTransferToLiveChat` | Service scheduling → live chat |
| `APPOINTMENT_PAYMENT_METHOD` | `isActivePaymentForAppointment` | Pay for service appointments in app |
| `R2_CONFIG_AVAILABLE` | `isR2ConfigurationAvailable` | R2 availability |
| `FEATURE_USAGE_TRACKING` | `featureUsageTracking` | Feature usage analytics |
| `VEHICLE_SERVICE_NOTIFICATIONS` | `vehicleServiceNotifications` | Service notification prompts |
| `INTERIOR_CAMERA` | `interiorCamera` | Interior camera features |
| `PRIVACY_PREFERENCE_CENTER` | `privacyPreferenceCenter` | Privacy preference center |

## Checking in code

Gates bundle one or more `wy/b` flags with an optional `VehicleFeature`. All app flags in the bundle must be enabled:

```text
FeatureGate.check(remoteConfigFlags: List<wy/b>, vehicleFeature: VehicleFeature?)
  → all remoteConfigFlags true in Firebase
  → if vehicleFeature set: SupportedFeatures[name] == AVAILABLE for vehicleId
```

See [Feature flags overview](/app/feature-flags) for vehicle-side names and Parallax combinations.
