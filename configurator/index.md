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
https://media.rivian.com/rivian-main/c_fill,w_1920/c_crop,h_1100,g_south,y_178/compositor/
```

## Example Image
```
https://media.rivian.com/rivian-main/c_fill,w_1920/c_crop,h_1100,g_south,y_178/compositor/r1s/front/2023.1,actbdg-brt,bat-c01,exp-lsv,gen-2,mot-201,pkg-adv,whl-2ss,studio
```
![R1S Example](https://media.rivian.com/rivian-main/c_fill,w_1920/c_crop,h_1100,g_south,y_178/compositor/r1s/front/2023.1,actbdg-brt,bat-c01,exp-lsv,gen-2,mot-201,pkg-adv,whl-2ss,studio)

## URL Structure (2023.1)
```
https://media.rivian.com/rivian-main/c_fill,w_1920/c_crop,h_1100,g_south,y_178/compositor/{vehicle}/{view}/{version},{options}
```

Where:
- `{vehicle}`: r1t or r1s
- `{view}`: front, rear, side, driver, backseats, studio
- `{version}`: 2023.1 (current version)
- `{options}`: comma-separated list of option codes (e.g., actbdg-brt,bat-c01,exp-lsv,gen-2,mot-201,pkg-adv,whl-2ss,studio)

## Views
```
front
rear
side
driver
backseats
studio
```

## Generation
```
GEN-1    Generation 1 (2021-2023)
GEN-2    Generation 2 (2024+)
```

## Option Codes
```
BUILD
  PKG-LCH	Launch Edition
  PKG-ADV	Adventure Package
  PKG-EXP	Explore Package
  PKG-ASC	Ascent Package

PAINT
  EXP-LSV	LA Silver
  EXP-GWT	Glacier White
  EXP-CRD	Red Canyon
  EXP-MDN	Midnight
  EXP-RBL	Rivian Blue
  EXP-LST	Limestone
  EXP-FGR	Forest Green
  EXP-LGR	Launch Green
  EXP-ELG	El Cap Granite
  EXP-CYL	Compass Yellow
  EXP-SBL	Storm Blue

WHEELS
  WHL-0A1	20" All-Terrain
  WHL-0AD	20" All-Terrain Dark
  WHL-0A2	20" All-Terrain Light (Discontinued)
  WHL-1RD	21" Road (Discontinued)
  WHL-2SS	22" Sport Bright
  WHL-2SD	22" Sport Dark
  WHL-2AR 22" Range
  WHL-0BS 20" All Season
  WHL-2SP 22" Super Sport
  WHL-2SB 22" Sport Burnished Bronze
  WHL-0DD 20" Dune Satin Graphite All-Terrain

INTERIOR
  INT-BMP	Black Mountain
  INT-GYP	Ocean Coast
  INT-GRP	Forest Edge

BATTERY
  BAT-C01	Standard Pack
  BAT-B01	Large Pack
  BAT-A01	Max Pack

MOTOR
  MOT-201	Dual-Motor
  MOT-301	Tri-Motor
  MOT-401	Quad-Motor

TRIM COLOR
  ACTBDG-BRT	Bright Package
  ACTBDG-DRK	Dark Package
```
