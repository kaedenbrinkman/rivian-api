---
title: Configurator API
has_children: false
nav_order: 2
---

# Configurator API

## Overview

The Rivian Configurator has an API for generating images of a particular configuration.

## Base URL
```
https://rivian.com/compimg/
```

## Example Image
```
https://rivian.com/compimg/r1s/2.2/us/exp-lgr_ord-ad3_pkg-lch_whl-1rd@3072x2688.front.webp
```
![R1S Example](https://rivian.com/compimg/r1s/2.2/us/exp-lgr_ord-ad3_pkg-lch_whl-1rd@3072x2688.front.webp)

## Views
```
front
rear
side
driver
backseats
```

## Option Codes

### R1 (R1T / R1S)

```
BUILD (PKG)
  PKG-LCH	Launch Edition
  PKG-ADV	Adventure
  PKG-ASC	Ascend
  PKG-EXP	Explore
BUILD (BLD)
  BLD-DSR1T / BLD-DSR1S	Dual Standard
  BLD-DR1T / BLD-DR1S	Dual
  BLD-TR1T / BLD-TR1S	Tri
  BLD-QLR1T / BLD-QLR1S	Quad Launch Edition
  BLD-QR1T / BLD-QR1S	Quad
PAINT
  EXP-LSV	LA Silver
  EXP-GWT	Glacier White
  EXP-CRD	Red Canyon
  EXP-MDN	Midnight
  EXP-RBL	Rivian Blue
  EXP-LST	Limestone
  EXP-FGR	Forest Green
  EXP-ELG	El Cap Granite
  EXP-SBL	Storm Blue
  EXP-CDN	California Dune (limited edition)
  EXP-LGR	Launch Green
  EXP-CYL	Compass Yellow
WHEELS
  WHL-0BS	20" All-Season
  WHL-0A1	20" All-Terrain
  WHL-0A2	20" All-Terrain Bright
  WHL-0AD	20" All-Terrain Dark
  WHL-0DD	20" Dune Satin Graphite All-Terrain
  WHL-0DN	20" Dune Color-Matched All-Terrain
  WHL-1RD	21" Road
  WHL-2SS	22" Sport Bright
  WHL-2SD	22" Sport Dark
  WHL-2AR	22" Range
  WHL-2SB	22" Sport Burnished Bronze
  WHL-2SP	22" Super Sport
  WHL-QAD	20" All-Terrain Burnished Bronze
INTERIOR
  INT-BMP	Black Mountain + Dark Ash Wood
  INT-PBMP	Black Mountain + Brown Ash Wood
  INT-GYP	Ocean Coast + Dark Ash Wood
  INT-OCDW	Ocean Coast + Driftwood
  INT-SSWW	Slate Sky + Walnut Wood
  INT-GRP	Forest Edge + Warm Ash Wood
  INT-GRP2	Forest Edge + Brown Ash Wood
  INT-SND	Sandstone + Dark Ash Wood
BATTERY
  BAT-C01	Standard
  BAT-B01 / BAT-LP01	Large
  BAT-A01	Max
  BAT-SP01	Standard+
MOTOR
  MOT-201 / MOT-202	Dual-motor AWD
  MOT-301	Tri-motor AWD
  MOT-401	Quad-motor AWD
  MOT-210	Performance Upgrade
```

### R2

```
BUILD / TRIM
  BLD-PRF2	R2 Performance
  BLD-PRM2	R2 Premium
  BLD-STND2	R2 Standard
PAINT
  EXP-GWT	Glacier White
  EXP-MDN	Midnight
  EXP-FGR	Forest Green
  EXP-LGR	Launch Green (Launch Package exclusive)
  EXP-BPR	Borealis
  EXP-ESV	Esker Silver
  EXP-HMG	Half Moon Grey
  EXP-CBL	Catalina Cove
WHEELS
  WHL-19A	19" Machined Graphite All-Season
  WHL-20AT	20" Black Sand All-Terrain
  WHL-20B	20" Bicolor Carbon All-Season
  WHL-21B	21" Liquid Tungsten All-Season
INTERIOR
  INT-PBC	Black Crater Signature
  INT-PCC	Coastal Cloud Signature
DRIVE SYSTEM (DTN codes)
  BLD-PRF2 / DTN-AWDP	R2 Performance All-Wheel Drive
  BLD-PRM2 / DTN-AWD	R2 Premium All-Wheel Drive
  BLD-STND2 / DTN-RWDS	R2 Standard Rear-Wheel Drive
  BLD-STND2 / DTN-RWD	R2 Standard Rear-Wheel Drive Long Range
  BLD-STND2 / DTN-AWDL	R2 Standard All-Wheel Drive Long Range
  BLD-STND2 / DTN-AWD	R2 Standard All-Wheel Drive Long Range
BATTERY
  BAT-SP01	Standard+
  BAT-LP01	Large
MOTOR
  MOT-202	Dual-motor AWD
  MOT-210	Performance Upgrade
```