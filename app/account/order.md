---
title: order
parent: Account Endpoints
has_children: false
nav_order: 3
---

# order

## Overview

The `order` endpoint returns details for a given order.

`POST https://rivian.com/api/gql/orders/graphql`

### Request Body

```json
{
  "operationName": "order",
  "variables": {
    "orderId": "<your-order-id>"
  },
  "query": "query order($id: String!) { order(id: $id) { vin state billingAddress { firstName lastName line1 line2 city state country postalCode } shippingAddress { firstName lastName line1 line2 city state country postalCode } orderCancelDate orderEmail currency locale storeId type subtotal discountTotal taxTotal feesTotal paidTotal remainingTotal outstandingBalance costAfterCredits total payments { id intent date method amount referenceNumber status card { last4 expiryDate brand } bank { bankName country last4 } transactionNotes } tradeIns { tradeInReferenceId amount } vehicle { vehicleId vin modelYear model make } items { id discounts { total items {  amount  title  code } } subtotal quantity title productId type unitPrice fees { items {  description  amount  code  type } total } taxes { items {  description  amount  code  rate  type } total } sku shippingAddress { firstName lastName line1 line2 city state country postalCode } configuration { ruleset {  meta {  rulesetId  storeId  country  vehicle  version  effectiveDate  currency  locale  availableLocales  }  defaults {  basePrice  initialSelection  }  groups  options  specs  rules } basePrice version options {  optionId  optionName  optionDetails {  name  attrs  price  visualExterior  visualInterior  hidden  disabled  required  }  groupId  groupName  groupDetails {  name  attrs  multiselect  required  options  }  price } } } }}"
}
```

### Example Response

```json
{
  "data": {
    "order": {
      "vin": null,
      "state": "ORDERED",
      "billingAddress": {
        "firstName": "<first name>",
        "lastName": "<last name>",
        "line1": "<street address>",
        "line2": null,
        "city": "<city>",
        "state": "<state>",
        "country": "<country>",
        "postalCode": "<zip>"
      },
      "shippingAddress": {
        "firstName": "<first name>",
        "lastName": "<last name>",
        "line1": "<street address>",
        "line2": null,
        "city": "<city>",
        "state": "<state>",
        "country": "<country>",
        "postalCode": "<zip>"
      },
      "orderCancelDate": null,
      "orderEmail": "<your-email-address>",
      "currency": "USD",
      "locale": "en-US",
      "storeId": "1",
      "type": "VEHICLE",
      "subtotal": 89250,
      "discountTotal": 0,
      "taxTotal": 5704.69,
      "feesTotal": 2160,
      "paidTotal": 10999.69,
      "remainingTotal": 86115,
      "outstandingBalance": 0,
      "costAfterCredits": 96114.69,
      "total": 97114.69,
      "payments": [
        {
          "id": "<payment id>",
          "intent": "DOWN_PAYMENT",
          "date": "<YYYY-MM-DDTHH:MM:SS.MMMZ>",
          "method": "ACH",
          "amount": 10000,
          "referenceNumber": null,
          "status": "SUCCEEDED",
          "card": null,
          "bank": null,
          "transactionNotes": null
        },
        {
          "id": "<payment id>",
          "intent": "DEPOSIT",
          "date": "<YYYY-MM-DDTHH:MM:SS.MMMZ>",
          "method": "CREDIT_CARD",
          "amount": 1000,
          "referenceNumber": null,
          "status": "SUCCEEDED",
          "card": {
            "last4": "<CC last 4>",
            "expiryDate": "<M/YYYY>",
            "brand": "<CC type>"
          },
          "bank": null,
          "transactionNotes": null
        },
        {
          "id": "<payment id>",
          "intent": "REMAINING_PAYMENT",
          "date": "<YYYY-MM-DDTHH:MM:SS.MMMZ>",
          "method": "THIRD_PARTY_FINANCING_ACH",
          "amount": 80000,
          "referenceNumber": null,
          "status": "PENDING",
          "card": null,
          "bank": null,
          "transactionNotes": "<Bank Name>"
        }
      ],
      "tradeIns": null,
      "vehicle": {
        "vehicleId": "<your-vehicle-id>",
        "vin": "<your-vin>",
        "modelYear": 2023,
        "model": "R1T",
        "make": "RIVIAN"
      },
      "items": [
        {
          "id": "<item-id>>",
          "discounts": null,
          "subtotal": 89250,
          "quantity": 1,
          "title": "Rivian R1T Truck",
          "productId": "95b3161c-ad1d-414f-9dc5-fdb971fca500",
          "type": "VEHICLE",
          "unitPrice": 89250,
          "fees": {
            "items": [
              {
                "description": "Registration Fee",
                "amount": 60,
                "code": "PLATE",
                "type": "dmv"
              },
              {
                "description": "Title Fee",
                "amount": 75,
                "code": "INITIAL_TITLE",
                "type": "dmv"
              },
              {
                "description": "Destination Fee",
                "amount": 1800,
                "code": "DELIVERY_FEE",
                "type": "VEHICLE"
              },
              {
                "description": "Documentation Fee",
                "amount": 225,
                "code": "DOCUMENTATION_FEE",
                "type": "VEHICLE"
              }
            ],
            "total": 2160
          },
          "taxes": {
            "items": [
              {
                "description": "Tax Rate",
                "amount": 0.0625,
                "code": "TAX_RATE",
                "rate": null,
                "type": "TaxRate"
              },
              {
                "description": "Net Sales Tax",
                "amount": 5704.69,
                "code": "NET_TAX",
                "rate": null,
                "type": "NetTax"
              },
              {
                "description": "Sales Tax Credit",
                "amount": 0,
                "code": "ST_CREDIT",
                "rate": null,
                "type": "Credit"
              },
              {
                "description": "Taxable Amount",
                "amount": 91275,
                "code": "TAXABLE_AMOUNT",
                "rate": null,
                "type": "TaxableAmount"
              },
              {
                "description": "Trade In Tax Credit",
                "amount": 0,
                "code": "TradeInTaxCredit",
                "rate": null,
                "type": "TradeInTaxCredit"
              }
            ],
            "total": 5704.69
          },
          "sku": "R1T",
          "shippingAddress": {
            "firstName": "<first name>",
            "lastName": "<last name>",
            "line1": "<street address>",
            "line2": null,
            "city": "<city>",
            "state": "<state>",
            "country": "<country>",
            "postalCode": "<zip>"
          },
          "configuration": {
            "ruleset": {
              "meta": {
                "rulesetId": "65be6937-f008-412c-877c-411d461ac9b1",
                "storeId": "1",
                "country": "<country>",
                "vehicle": "R1T",
                "version": "2.6",
                "effectiveDate": "<YYYY-MM-DDTHH:MM:SS.MMMZ>",
                "currency": "USD",
                "locale": "en-US",
                "availableLocales": [
                  "en-US"
                ]
              },
              "defaults": {
                "basePrice": 67500,
                "initialSelection": [
                  "PKG-LCH",
                  "RGN-USA"
                ]
              },
              "groups": {
                "MOT": {
                  "fullName": {
                    "en-US": "Drive system"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Drive system"
                    },
                    "gaKey": "Motor"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "MOT-201",
                    "MOT-401"
                  ]
                },
                "BAT": {
                  "fullName": {
                    "en-US": "Battery"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Battery"
                    },
                    "gaKey": "Range"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "BAT-C01",
                    "BAT-B01",
                    "BAT-A01"
                  ]
                },
                "PPW": {
                  "fullName": {
                    "en-US": "Wraps"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Wraps"
                    },
                    "gaKey": "Wraps"
                  },
                  "multiselect": false,
                  "required": false,
                  "options": [
                    "PPW-FG1"
                  ]
                },
                "RGN": {
                  "fullName": {
                    "en-US": "Region"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "RGN-USA"
                  ]
                },
                "WHL": {
                  "fullName": {
                    "en-US": "Wheels and tires"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Wheels and tires"
                    },
                    "description": {
                      "en-US": "20\" and 22\" wheels reduce estimated range."
                    },
                    "gaKey": "Wheels"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "WHL-0A1",
                    "WHL-0A2",
                    "WHL-0AD",
                    "WHL-1RD",
                    "WHL-2SS",
                    "WHL-2SD"
                  ]
                },
                "ACCESSORIES": {
                  "fullName": {
                    "en-US": "Adventure Gear"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Adventure Gear"
                    },
                    "gaKey": "Accessories"
                  },
                  "multiselect": true,
                  "required": false,
                  "options": [
                    "ORD-AD2",
                    "ORD-AD3",
                    "SWH-0A1",
                    "SWH-0A2",
                    "SWH-0AD",
                    "SWH-1RD",
                    "SWH-2SS",
                    "SWH-2SD",
                    "ACERORB001",
                    "ACERAWM002",
                    "ACERRK0001",
                    "ACERFK0003",
                    "TON-M01",
                    "TON-P01",
                    "ACERKSU001",
                    "ACERRTT001",
                    "ACERRTT002",
                    "ACERGTS001",
                    "ACERCSB003",
                    "ACERBM0001",
                    "ACERSSM001",
                    "ACERKM0001",
                    "ACERSM0001",
                    "ACERCWB001",
                    "ACERWC0003",
                    "ACERORM001"
                  ]
                },
                "EXP": {
                  "fullName": {
                    "en-US": "Paint"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Paint"
                    },
                    "gaKey": "Exterior"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "EXP-LGR",
                    "EXP-LSV",
                    "EXP-GWT",
                    "EXP-CRD",
                    "EXP-MDN",
                    "EXP-RBL",
                    "EXP-LST",
                    "EXP-FGR",
                    "EXP-ELG",
                    "EXP-CYL"
                  ]
                },
                "PKG": {
                  "fullName": {
                    "en-US": "Package"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Package"
                    },
                    "gaKey": "Trim"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "PKG-LCH",
                    "PKG-ADV"
                  ]
                },
                "INT": {
                  "fullName": {
                    "en-US": "Interior"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Color options"
                    },
                    "gaKey": "Interior",
                    "longTitle": {
                      "en-US": "Interior"
                    }
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "INT-BMV",
                    "INT-GYV",
                    "INT-BMP",
                    "INT-GYP",
                    "INT-GRP"
                  ]
                }
              },
              "options": {
                "ACERKSU001": {
                  "fullName": {
                    "en-US": "Rivian Camp Kitchen x Snow Peak"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Rivian Camp Kitchen x Snow Peak"
                    },
                    "description": {
                      "en-US": "A complete cooking system for any adventure."
                    },
                    "gaKey": "Camp Kitchen"
                  },
                  "price": 6750,
                  "visualExterior": true,
                  "hidden": true,
                  "disabled": true,
                  "tempUnavailable": true
                },
                "EXP-ELG": {
                  "fullName": {
                    "en-US": "El Cap Granite exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "El Cap Granite"
                    },
                    "gaKey": "El Cap Granite Exterior",
                    "genericTitle": {
                      "en-US": "Grey"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "RGN-USA": {
                  "fullName": {
                    "en-US": "United States of America"
                  },
                  "price": 0,
                  "hidden": true
                },
                "TON-P01": {
                  "fullName": {
                    "en-US": "Powered Tonneau Cover"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Powered Tonneau Cover"
                    },
                    "gaKey": "Powered Tonneau Cover"
                  },
                  "price": 3000,
                  "hidden": true
                },
                "ACERCWB001": {
                  "fullName": {
                    "en-US": "Wall Charger"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Wall Charger"
                    },
                    "description": {
                      "en-US": "The Rivian Wall Charger is the fastest way to charge your Rivian at home — delivering up to 25 miles of range every hour of charging."
                    },
                    "gaKey": "Wall Charger"
                  },
                  "price": 750,
                  "hidden": true,
                  "orderItem": true,
                  "availability": [
                    "DISCONTINUED"
                  ]
                },
                "WHL-2SD": {
                  "fullName": {
                    "en-US": "22\" Sport Dark wheel and tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Machined aluminum wheel with high gloss black pockets and a tinted clearcoat."
                    },
                    "title": {
                      "en-US": "22\" Sport Dark"
                    },
                    "gaKey": "22\" Sport Dark Wheels",
                    "longTitle": {
                      "en-US": "22\" Sport Dark wheels"
                    }
                  },
                  "price": 3500,
                  "visualExterior": true
                },
                "SWH-2SS": {
                  "fullName": {
                    "en-US": "Full-size spare tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "A matching tire and wheel stored under the bed. Includes the tools to change your tire when you need it."
                    },
                    "tag": {
                      "en-US": "22\" Sport Bright"
                    },
                    "title": {
                      "en-US": "Full-size spare"
                    },
                    "gaKey": "Spare Tire, matching 22\" Sport Bright Wheels"
                  },
                  "price": 900,
                  "hidden": true
                },
                "BAT-B01": {
                  "fullName": {
                    "en-US": "Large battery pack"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Large pack"
                    },
                    "gaKey": "Large pack"
                  },
                  "price": 6000
                },
                "INT-BMP": {
                  "fullName": {
                    "en-US": "Black Mountain + Dark Ash Wood interior"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Black Mountain + Dark Ash Wood"
                    },
                    "gaKey": "Black Mountain + Dark Ash Wood interior"
                  },
                  "price": 0,
                  "visualInterior": true
                },
                "ACERGTS001": {
                  "fullName": {
                    "en-US": "Gear Tunnel Shuttle"
                  },
                  "attrs": {
                    "requiredNote": {
                      "en-US": "Included with Camp Kitchen"
                    },
                    "description": {
                      "en-US": "A slide-out platform to maximize the utility of your Gear Tunnel."
                    },
                    "title": {
                      "en-US": "Gear Tunnel Shuttle"
                    },
                    "gaKey": "Gear Tunnel Shuttle"
                  },
                  "price": 1500,
                  "visualExterior": true,
                  "hidden": true,
                  "disabled": true,
                  "tempUnavailable": true
                },
                "PKG-ADV": {
                  "fullName": {
                    "en-US": "Adventure Package"
                  },
                  "attrs": {
                    "features": [
                      {
                        "key": "gearGuard",
                        "text": {
                          "en-US": "Gear Guard security cable"
                        }
                      },
                      {
                        "key": "compressor",
                        "text": {
                          "en-US": "Air compressor"
                        }
                      },
                      {
                        "key": "towhooks",
                        "text": {
                          "en-US": "Dual front bumper tow hooks"
                        }
                      },
                      {
                        "key": "sound",
                        "text": {
                          "en-US": "Rivian Elevation audio by Meridian"
                        }
                      },
                      {
                        "key": "leather",
                        "text": {
                          "en-US": "Perforated vegan leather seating with patterned stitching"
                        }
                      },
                      {
                        "key": "seats",
                        "text": {
                          "en-US": "Heated and ventilated seats"
                        }
                      },
                      {
                        "key": "steering",
                        "text": {
                          "en-US": "Heated steering wheel"
                        }
                      },
                      {
                        "key": "lumbarAdj",
                        "text": {
                          "en-US": "Driver and passenger lumbar adjustment"
                        }
                      },
                      {
                        "key": "accents",
                        "text": {
                          "en-US": "Compass Yellow interior accents"
                        }
                      },
                      {
                        "key": "headliner",
                        "text": {
                          "en-US": "100% recycled microfiber headliner"
                        }
                      },
                      {
                        "key": "floormats",
                        "text": {
                          "en-US": "Chilewich floor mats"
                        }
                      }
                    ],
                    "title": {
                      "en-US": "Adventure"
                    },
                    "gaKey": "Adventure Package",
                    "longTitle": {
                      "en-US": "Adventure Package"
                    }
                  },
                  "price": 5500,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "MOT-401": {
                  "fullName": {
                    "en-US": "Quad-Motor AWD"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Quad-Motor AWD"
                    },
                    "features": [
                      {
                        "key": "drivetrain",
                        "text": {
                          "en-US": "All-wheel drive"
                        }
                      },
                      {
                        "key": "motors",
                        "text": {
                          "en-US": "One motor per wheel"
                        }
                      },
                      {
                        "key": "acceleration",
                        "text": {
                          "en-US": "0–60 mph as quick as 3.0 seconds¹"
                        }
                      },
                      {
                        "key": "power",
                        "text": {
                          "en-US": "More than 800 horsepower"
                        }
                      },
                      {
                        "key": "torque",
                        "text": {
                          "en-US": "More than 900 ft lbs of torque"
                        }
                      }
                    ],
                    "gaKey": "Quad-Motor AWD"
                  },
                  "price": 6000
                },
                "INT-BMV": {
                  "fullName": {
                    "en-US": "Black Mountain interior"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Black Mountain"
                    },
                    "gaKey": "Black Mountain interior"
                  },
                  "price": 0,
                  "visualInterior": true
                },
                "MOT-201": {
                  "fullName": {
                    "en-US": "Dual-Motor AWD"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "(Coming mid-2023)"
                    },
                    "features": [
                      {
                        "key": "drivetrain",
                        "text": {
                          "en-US": "All-wheel drive"
                        }
                      },
                      {
                        "key": "motors",
                        "text": {
                          "en-US": "One motor per axle"
                        }
                      },
                      {
                        "key": "acceleration",
                        "text": {
                          "en-US": "0–60 mph as quick as 4.5 seconds¹"
                        }
                      },
                      {
                        "key": "power",
                        "text": {
                          "en-US": "More than 600 horsepower¹"
                        }
                      },
                      {
                        "key": "torque",
                        "text": {
                          "en-US": "More than 600 ft lbs of torque¹"
                        }
                      }
                    ],
                    "title": {
                      "en-US": "Dual-Motor AWD"
                    },
                    "gaKey": "Dual-Motor AWD",
                    "disabledNote": {
                      "en-US": "Not available with Launch Edition"
                    }
                  },
                  "price": 0
                },
                "SWH-1RD": {
                  "fullName": {
                    "en-US": "Full-size spare tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "A matching tire and wheel stored under the bed. Includes the tools to change your tire when you need it."
                    },
                    "tag": {
                      "en-US": "21\" Road"
                    },
                    "title": {
                      "en-US": "Full-size spare"
                    },
                    "gaKey": "Spare Tire, matching 21\" Road Wheels"
                  },
                  "price": 750,
                  "hidden": true
                },
                "ACERRTT001": {
                  "fullName": {
                    "en-US": "Three-Person Tent - Pewter"
                  },
                  "attrs": {
                    "colorName": {
                      "en-US": "Pewter"
                    },
                    "description": {
                      "en-US": "Sleep under the stars in a custom tent designed with Yakima."
                    },
                    "colorCode": "#656768",
                    "title": {
                      "en-US": "Three-Person Tent + Cargo Crossbars + Brake Light Accessory"
                    },
                    "gaKey": "Three-Person Tent - Pewter",
                    "groupingKey": "ROOFTOP_TENT",
                    "longTitle": {
                      "en-US": "Three-Person Tent - Pewter"
                    }
                  },
                  "price": 3100,
                  "visualExterior": true,
                  "hidden": true,
                  "disabled": true,
                  "tempUnavailable": true,
                  "orderItem": true
                },
                "ACERRTT002": {
                  "fullName": {
                    "en-US": "Three-Person Tent - Yellow"
                  },
                  "attrs": {
                    "colorName": {
                      "en-US": "Yellow"
                    },
                    "description": {
                      "en-US": "Sleep under the stars in a custom tent designed with Yakima."
                    },
                    "colorCode": "#ffb100",
                    "title": {
                      "en-US": "Three-Person Tent + Cargo Crossbars + Brake Light Accessory"
                    },
                    "gaKey": "Three-Person Tent - Yellow",
                    "groupingKey": "ROOFTOP_TENT",
                    "longTitle": {
                      "en-US": "Three-Person Tent - Yellow"
                    }
                  },
                  "price": 3100,
                  "visualExterior": true,
                  "hidden": true,
                  "disabled": true,
                  "tempUnavailable": true,
                  "orderItem": true
                },
                "ACERSM0001": {
                  "fullName": {
                    "en-US": "SUP/Surfboard Mount"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "SUP/Surfboard Mount"
                    },
                    "gaKey": "SUP/Surfboard Mount",
                    "disabledNote": {
                      "en-US": "Requires Crossbars"
                    }
                  },
                  "price": 300,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "EXP-GWT": {
                  "fullName": {
                    "en-US": "Glacier White exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Glacier White"
                    },
                    "gaKey": "Glacier White Exterior",
                    "genericTitle": {
                      "en-US": "White"
                    }
                  },
                  "price": 1750,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "ACERBM0001": {
                  "fullName": {
                    "en-US": "Rooftop Bike Mount"
                  },
                  "attrs": {
                    "priceNote": {
                      "en-US": "Each"
                    },
                    "title": {
                      "en-US": "Rooftop Bike Mount"
                    },
                    "gaKey": "Bike Mount",
                    "disabledNote": {
                      "en-US": "Requires Crossbars"
                    }
                  },
                  "price": 270,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true,
                  "limit": 4
                },
                "ORD-AD3": {
                  "fullName": {
                    "en-US": "Tow Hooks"
                  },
                  "attrs": {
                    "requiredNote": {
                      "en-US": "Included with package"
                    },
                    "description": {
                      "en-US": "Dual, front bumper tow hooks make for quick and easy towing off the beaten path."
                    },
                    "title": {
                      "en-US": "Tow Hooks"
                    },
                    "gaKey": "Tow Hooks"
                  },
                  "price": 0,
                  "visualExterior": true,
                  "hidden": true
                },
                "WHL-1RD": {
                  "fullName": {
                    "en-US": "21\" Road wheel and tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Machined aluminum wheel with painted high gloss anthracite."
                    },
                    "title": {
                      "en-US": "21\" Road"
                    },
                    "gaKey": "21\" Road Wheels",
                    "longTitle": {
                      "en-US": "21\" Road wheels"
                    }
                  },
                  "price": 0,
                  "visualExterior": true
                },
                "ORD-AD2": {
                  "fullName": {
                    "en-US": "Reinforced Underbody Shield"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Reinforced Underbody Shield"
                    },
                    "description": {
                      "en-US": "Engineered to absorb, deflect and distribute impacts in extreme off-road conditions."
                    },
                    "gaKey": "Reinforced Underbody Shield"
                  },
                  "price": 2000
                },
                "INT-GRP": {
                  "fullName": {
                    "en-US": "Forest Edge + Warm Ash Wood interior"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Forest Edge + Warm Ash Wood"
                    },
                    "gaKey": "Forest Edge + Warm Ash Wood interior"
                  },
                  "price": 2000,
                  "visualInterior": true
                },
                "ACERCSB003": {
                  "fullName": {
                    "en-US": "Cargo Crossbars"
                  },
                  "attrs": {
                    "requiredNote": {
                      "en-US": "Included with tent package"
                    },
                    "description": {
                      "en-US": "Designed specifically for your Rivian, the Cargo Crossbars are extremely easy to lock-on to your vehicle’s accessory ports."
                    },
                    "priceNote": {
                      "en-US": "Per pair"
                    },
                    "title": {
                      "en-US": "Cargo Crossbars"
                    },
                    "gaKey": "Cargo Crossbars"
                  },
                  "price": 500,
                  "visualExterior": true,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "SWH-2SD": {
                  "fullName": {
                    "en-US": "Full-size spare tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "A matching tire and wheel stored under the bed. Includes the tools to change your tire when you need it."
                    },
                    "tag": {
                      "en-US": "22\" Sport Dark"
                    },
                    "title": {
                      "en-US": "Full-size spare"
                    },
                    "gaKey": "Spare Tire, matching 22\" Sport Dark Wheels"
                  },
                  "price": 1000,
                  "hidden": true
                },
                "ACERKM0001": {
                  "fullName": {
                    "en-US": "Kayak Mount"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Kayak Mount"
                    },
                    "gaKey": "Kayak Mount",
                    "disabledNote": {
                      "en-US": "Requires Crossbars"
                    }
                  },
                  "price": 230,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "WHL-2SS": {
                  "fullName": {
                    "en-US": "22\" Sport Bright wheel and tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Machined aluminum wheel with high gloss black pockets."
                    },
                    "title": {
                      "en-US": "22\" Sport Bright"
                    },
                    "gaKey": "22\" Sport Bright Wheels",
                    "longTitle": {
                      "en-US": "22\" Sport Bright wheels"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true
                },
                "ACERORM001": {
                  "fullName": {
                    "en-US": "Rivian x MAXTRAX Recovery Board Mount"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Rivian x MAXTRAX Recovery Board Mount"
                    },
                    "gaKey": "Recovery Board Mount",
                    "longTitle": {
                      "en-US": "Rivian x MAXTRAX Recovery Board Mount"
                    },
                    "disabledNote": {
                      "en-US": "Requires Crossbars"
                    }
                  },
                  "price": 115,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "SWH-0AD": {
                  "fullName": {
                    "en-US": "Full-size spare tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "A matching tire and wheel stored under the bed. Includes the tools to change your tire when you need it."
                    },
                    "tag": {
                      "en-US": "20\" All-Terrain Dark"
                    },
                    "title": {
                      "en-US": "Full-size spare"
                    },
                    "gaKey": "Spare Tire, matching 20\" All-Terrain Dark Wheels"
                  },
                  "price": 1000,
                  "hidden": true
                },
                "ACERORB001": {
                  "fullName": {
                    "en-US": "Rivian x MAXTRAX Recovery Boards"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Our signature set of MAXTRAX XTREME Recovery Boards comes in black with black teeth for traction when null exists."
                    },
                    "priceNote": {
                      "en-US": "Per pair"
                    },
                    "title": {
                      "en-US": "Rivian x MAXTRAX Recovery Boards"
                    },
                    "gaKey": "Recovery Boards"
                  },
                  "price": 500,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "TON-M01": {
                  "fullName": {
                    "en-US": "Manual Tonneau Cover"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Manual Tonneau Cover"
                    },
                    "description": {
                      "en-US": "The tonneau cover has four interlocking panels that slide in the channel of the truck bed. It comes with a bag and stores easily inside the Gear Tunnel.\n\nExpected to ship separately in mid-2023."
                    },
                    "gaKey": "Manual Tonneau Cover"
                  },
                  "price": 1800
                },
                "PPW-FG1": {
                  "fullName": {
                    "en-US": "Front Paint Protection"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Protect your vehicle from rock chips and scratches with XPEL paint protection film."
                    },
                    "title": {
                      "en-US": "Paint Protection"
                    },
                    "variantName": {
                      "en-US": "Front"
                    },
                    "gaKey": "Front Paint Protection",
                    "groupingKey": "PAINT_PROTECTION",
                    "longTitle": {
                      "en-US": "Front Paint Protection"
                    }
                  },
                  "price": 1500,
                  "visualExterior": false,
                  "visualInterior": false
                },
                "EXP-CRD": {
                  "fullName": {
                    "en-US": "Red Canyon exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Red Canyon"
                    },
                    "gaKey": "Red Canyon Exterior",
                    "genericTitle": {
                      "en-US": "Red"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "WHL-0A2": {
                  "fullName": {
                    "en-US": "20\" All-Terrain Bright wheel and tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Machined aluminum wheel with high gloss black pockets."
                    },
                    "title": {
                      "en-US": "20\" All-Terrain Bright"
                    },
                    "gaKey": "20\" All-Terrain Bright Wheels",
                    "longTitle": {
                      "en-US": "20\" All-Terrain Bright wheels"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true
                },
                "INT-GYV": {
                  "fullName": {
                    "en-US": "Ocean Coast interior"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Ocean Coast"
                    },
                    "gaKey": "Ocean Coast interior"
                  },
                  "price": 2000,
                  "visualInterior": true
                },
                "BAT-A01": {
                  "fullName": {
                    "en-US": "Max battery pack"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Max pack"
                    },
                    "gaKey": "Max pack",
                    "disabledNote": {
                      "en-US": "Not available with Launch Edition"
                    }
                  },
                  "price": 16000
                },
                "WHL-0A1": {
                  "fullName": {
                    "en-US": "20\" All-Terrain wheel and tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Machined aluminum wheel with painted low gloss anthracite."
                    },
                    "title": {
                      "en-US": "20\" All-Terrain"
                    },
                    "gaKey": "20\" All-Terrain Wheels",
                    "longTitle": {
                      "en-US": "20\" All-Terrain wheels"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true
                },
                "EXP-LGR": {
                  "fullName": {
                    "en-US": "Launch Green exterior color"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Exclusive"
                    },
                    "title": {
                      "en-US": "Launch Green"
                    },
                    "gaKey": "Launch Green Exterior",
                    "genericTitle": {
                      "en-US": "Green"
                    },
                    "disabledNote": {
                      "en-US": "Available with Launch Edition"
                    }
                  },
                  "price": 0,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "EXP-FGR": {
                  "fullName": {
                    "en-US": "Forest Green exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Forest Green"
                    },
                    "gaKey": "Forest Green Exterior",
                    "genericTitle": {
                      "en-US": "Green"
                    }
                  },
                  "price": 1750,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "INT-GYP": {
                  "fullName": {
                    "en-US": "Ocean Coast + Dark Ash Wood interior"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Ocean Coast + Dark Ash Wood"
                    },
                    "gaKey": "Ocean Coast + Dark Ash Wood interior"
                  },
                  "price": 2000,
                  "visualInterior": true
                },
                "BAT-C01": {
                  "fullName": {
                    "en-US": "Standard battery pack"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "(Coming 2024)"
                    },
                    "title": {
                      "en-US": "Standard pack"
                    },
                    "gaKey": "Standard pack",
                    "disabledNote": {
                      "en-US": "Not available with Quad-Motor AWD"
                    }
                  },
                  "price": 0
                },
                "ACERAWM002": {
                  "fullName": {
                    "en-US": "All-Weather Floor Mats"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "All-Weather Floor Mats"
                    },
                    "description": {
                      "en-US": "Fully integrated to fully protect your Rivian."
                    },
                    "gaKey": "All-Weather Floor Mats"
                  },
                  "price": 200,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "ACERWC0003": {
                  "fullName": {
                    "en-US": "Wall Charger"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Wall Charger"
                    },
                    "description": {
                      "en-US": "The Rivian Wall Charger is the fastest way to charge your Rivian at home — delivering up to 25 miles of range every hour of charging."
                    },
                    "gaKey": "Wall Charger"
                  },
                  "price": 750,
                  "orderItem": true
                },
                "ACERSSM001": {
                  "fullName": {
                    "en-US": "Snowboard/Ski Mount"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Snowboard/Ski Mount"
                    },
                    "gaKey": "Snowboard/Ski Mount",
                    "disabledNote": {
                      "en-US": "Requires Crossbars"
                    }
                  },
                  "price": 340,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "EXP-LST": {
                  "fullName": {
                    "en-US": "Limestone exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Limestone"
                    },
                    "gaKey": "Limestone Exterior",
                    "genericTitle": {
                      "en-US": "Grey"
                    }
                  },
                  "price": 1750,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "ACERRK0001": {
                  "fullName": {
                    "en-US": "Off-Road Recovery Kit"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Off-Road Recovery Kit"
                    },
                    "description": {
                      "en-US": "A kit to help get you moving again."
                    },
                    "gaKey": "Off-Road Recovery Kit"
                  },
                  "price": 600,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "EXP-LSV": {
                  "fullName": {
                    "en-US": "LA Silver exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "LA Silver"
                    },
                    "gaKey": "LA Silver Exterior",
                    "genericTitle": {
                      "en-US": "Silver"
                    }
                  },
                  "price": 0,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "SWH-0A1": {
                  "fullName": {
                    "en-US": "Full-size spare tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "A matching tire and wheel stored under the bed. Includes the tools to change your tire when you need it."
                    },
                    "tag": {
                      "en-US": "20\" All-Terrain"
                    },
                    "title": {
                      "en-US": "Full-size spare"
                    },
                    "gaKey": "Spare Tire, matching 20\" All-Terrain Wheels"
                  },
                  "price": 900,
                  "hidden": true
                },
                "EXP-MDN": {
                  "fullName": {
                    "en-US": "Midnight exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Midnight"
                    },
                    "gaKey": "Midnight Exterior",
                    "genericTitle": {
                      "en-US": "Black"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "EXP-CYL": {
                  "fullName": {
                    "en-US": "Compass Yellow exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Compass Yellow"
                    },
                    "gaKey": "Compass Yellow Exterior",
                    "genericTitle": {
                      "en-US": "Yellow"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "EXP-RBL": {
                  "fullName": {
                    "en-US": "Rivian Blue exterior color"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Rivian Blue"
                    },
                    "gaKey": "Rivian Blue Exterior",
                    "genericTitle": {
                      "en-US": "Blue"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true,
                  "visualInterior": true
                },
                "PKG-LCH": {
                  "fullName": {
                    "en-US": "Launch Edition"
                  },
                  "attrs": {
                    "availabilityNote": {
                      "en-US": "Reservations full"
                    },
                    "features": [
                      {
                        "key": "gearGuard",
                        "text": {
                          "en-US": "Gear Guard security cable"
                        }
                      },
                      {
                        "key": "compressor",
                        "text": {
                          "en-US": "Air compressor"
                        }
                      },
                      {
                        "key": "towhooks",
                        "text": {
                          "en-US": "Dual front bumper tow hooks"
                        }
                      },
                      {
                        "key": "sound",
                        "text": {
                          "en-US": "Rivian Elevation audio by Meridian"
                        }
                      },
                      {
                        "key": "finish",
                        "text": {
                          "en-US": "Natural-grained ash wood interior finishes"
                        }
                      },
                      {
                        "key": "leather",
                        "text": {
                          "en-US": "Perforated vegan leather seating with patterned stitching"
                        }
                      },
                      {
                        "key": "seats",
                        "text": {
                          "en-US": "Heated and ventilated seats"
                        }
                      },
                      {
                        "key": "steering",
                        "text": {
                          "en-US": "Heated steering wheel"
                        }
                      },
                      {
                        "key": "lumbarAdj",
                        "text": {
                          "en-US": "Driver and passenger lumbar adjustment"
                        }
                      },
                      {
                        "key": "accents",
                        "text": {
                          "en-US": "Compass Yellow interior accents"
                        }
                      },
                      {
                        "key": "headliner",
                        "text": {
                          "en-US": "100% recycled microfiber headliner"
                        }
                      },
                      {
                        "key": "floormats",
                        "text": {
                          "en-US": "Chilewich floor mats"
                        }
                      }
                    ],
                    "title": {
                      "en-US": "Launch Edition"
                    },
                    "gaKey": "Launch Edition",
                    "exclusiveFeatures": [
                      {
                        "key": "delivery",
                        "text": {
                          "en-US": "Priority delivery"
                        }
                      },
                      {
                        "key": "battery",
                        "text": {
                          "en-US": "Large battery pack included"
                        }
                      },
                      {
                        "key": "badges",
                        "text": {
                          "en-US": "Launch Edition interior badging"
                        }
                      },
                      {
                        "key": "color",
                        "text": {
                          "en-US": "Special Launch Green paint color option"
                        }
                      },
                      {
                        "key": "wheels",
                        "text": {
                          "en-US": "20” All-Terrain or 22” Sport wheel upgrade included"
                        }
                      },
                      {
                        "key": "motor",
                        "text": {
                          "en-US": "Quad-Motor AWD included"
                        }
                      }
                    ]
                  },
                  "price": 14500,
                  "visualExterior": true,
                  "visualInterior": true,
                  "availability": [
                    "EXISTING_CONFIGURATION"
                  ]
                },
                "SWH-0A2": {
                  "fullName": {
                    "en-US": "Full-size spare tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "A matching tire and wheel stored under the bed. Includes the tools to change your tire when you need it."
                    },
                    "tag": {
                      "en-US": "20\" All-Terrain Bright"
                    },
                    "title": {
                      "en-US": "Full-size spare"
                    },
                    "gaKey": "Spare Tire, matching 20\" All-Terrain Bright Wheels"
                  },
                  "price": 900,
                  "hidden": true
                },
                "ACERFK0003": {
                  "fullName": {
                    "en-US": "Field Kit"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Field Kit"
                    },
                    "description": {
                      "en-US": "A comprehensive kit for any kind of emergency."
                    },
                    "gaKey": "Field Kit"
                  },
                  "price": 150,
                  "hidden": true,
                  "disabled": true,
                  "orderItem": true
                },
                "WHL-0AD": {
                  "fullName": {
                    "en-US": "20\" All-Terrain Dark wheel and tire"
                  },
                  "attrs": {
                    "description": {
                      "en-US": "Machined aluminum wheel with high gloss black pockets and a tinted clearcoat."
                    },
                    "title": {
                      "en-US": "20\" All-Terrain Dark"
                    },
                    "gaKey": "20\" All-Terrain Dark Wheels",
                    "longTitle": {
                      "en-US": "20\" All-Terrain Dark wheels"
                    }
                  },
                  "price": 3500,
                  "visualExterior": true
                }
              },
              "specs": {
                "range": {
                  "fullName": {
                    "en-US": "Range"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Estimated range"
                    },
                    "suffix": {
                      "en-US": " mi"
                    },
                    "units": {
                      "en-US": "mi"
                    }
                  },
                  "value": "328"
                },
                "storage": {
                  "fullName": {
                    "en-US": "Storage"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Storage"
                    },
                    "suffix": {
                      "en-US": " cu ft"
                    },
                    "units": {
                      "en-US": "cu ft"
                    }
                  },
                  "value": "68"
                },
                "seats": {
                  "fullName": {
                    "en-US": "Seats"
                  },
                  "attrs": {
                    "title": {
                      "en-US": "Seats"
                    }
                  },
                  "value": "5"
                },
                "epa": {
                  "fullName": {
                    "en-US": "EPA est."
                  },
                  "attrs": {
                    "title": {
                      "en-US": "EPA est."
                    }
                  },
                  "value": "true"
                }
              },
              "rules": [
                {
                  "when": {
                    "is": "set",
                    "option": "PKG-LCH"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": true,
                        "option": "BAT-A01"
                      },
                      {
                        "price": 0,
                        "option": "WHL-2SS"
                      },
                      {
                        "price": 0,
                        "option": "WHL-0A1"
                      },
                      {
                        "price": 0,
                        "option": "WHL-0A2"
                      },
                      {
                        "disabled": false,
                        "option": "EXP-LGR"
                      },
                      {
                        "price": 0,
                        "option": "BAT-B01"
                      },
                      {
                        "disabled": true,
                        "price": 0,
                        "option": "BAT-A01"
                      },
                      {
                        "disabled": true,
                        "option": "MOT-201"
                      },
                      {
                        "price": 0,
                        "option": "MOT-401"
                      },
                      {
                        "required": true,
                        "option": "ORD-AD3"
                      },
                      {
                        "hidden": true,
                        "disabled": true,
                        "option": "INT-BMV"
                      },
                      {
                        "hidden": true,
                        "disabled": true,
                        "option": "INT-GYV"
                      }
                    ],
                    "select": [
                      "EXP-LGR",
                      "INT-BMP",
                      "BAT-B01",
                      "MOT-401",
                      "WHL-0A1",
                      "ORD-AD3"
                    ],
                    "unselect": [
                      "ORD-AD2",
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD",
                      "PPW-FG1",
                      "TON-M01",
                      "TON-P01",
                      "ACERWC0003"
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "PKG-ADV"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": false,
                        "option": "BAT-A01"
                      },
                      {
                        "price": 2500,
                        "option": "WHL-2SS"
                      },
                      {
                        "price": 2500,
                        "option": "WHL-0A1"
                      },
                      {
                        "price": 2500,
                        "option": "WHL-0A2"
                      },
                      {
                        "disabled": true,
                        "option": "EXP-LGR"
                      },
                      {
                        "price": 6000,
                        "option": "BAT-B01"
                      },
                      {
                        "disabled": false,
                        "price": 16000,
                        "option": "BAT-A01"
                      },
                      {
                        "disabled": false,
                        "option": "MOT-201"
                      },
                      {
                        "price": 6000,
                        "option": "MOT-401"
                      },
                      {
                        "required": true,
                        "option": "ORD-AD3"
                      },
                      {
                        "hidden": false,
                        "disabled": false,
                        "option": "INT-BMV"
                      },
                      {
                        "hidden": false,
                        "disabled": false,
                        "option": "INT-GYV"
                      }
                    ],
                    "select": [
                      "EXP-LSV",
                      "INT-BMV",
                      "BAT-B01",
                      "WHL-1RD",
                      "MOT-401",
                      "ORD-AD3"
                    ],
                    "unselect": [
                      "ORD-AD2",
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD",
                      "TON-M01",
                      "TON-P01",
                      "PPW-FG1",
                      "ACERWC0003"
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "BAT-A01"
                  },
                  "then": {
                    "update": [
                      {
                        "value": "67",
                        "spec": "storage"
                      }
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "BAT-B01"
                  },
                  "then": {
                    "update": [
                      {
                        "value": "68",
                        "spec": "storage"
                      }
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "BAT-C01"
                  },
                  "then": {
                    "update": [
                      {
                        "value": "68",
                        "spec": "storage"
                      }
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "MOT-401"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": true,
                        "option": "BAT-C01"
                      }
                    ],
                    "select": [
                      "BAT-B01"
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "unset",
                      "option": "MOT-401"
                    },
                    {
                      "is": "unset",
                      "option": "PKG-LCH"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "disabled": false,
                        "option": "BAT-C01"
                      }
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "WHL-0A1"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": false,
                        "option": "SWH-0A1"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0A2"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0AD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-1RD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SS"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SD"
                      }
                    ],
                    "unselect": [
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD"
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "WHL-0A2"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": true,
                        "option": "SWH-0A1"
                      },
                      {
                        "disabled": false,
                        "option": "SWH-0A2"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0AD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-1RD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SS"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SD"
                      }
                    ],
                    "unselect": [
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD"
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "WHL-0AD"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": true,
                        "option": "SWH-0A1"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0A2"
                      },
                      {
                        "disabled": false,
                        "option": "SWH-0AD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-1RD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SS"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SD"
                      }
                    ],
                    "unselect": [
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD"
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "WHL-1RD"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": true,
                        "option": "SWH-0A1"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0A2"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0AD"
                      },
                      {
                        "disabled": false,
                        "option": "SWH-1RD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SS"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SD"
                      }
                    ],
                    "unselect": [
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD"
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "WHL-2SS"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": true,
                        "option": "SWH-0A1"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0A2"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0AD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-1RD"
                      },
                      {
                        "disabled": false,
                        "option": "SWH-2SS"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SD"
                      }
                    ],
                    "unselect": [
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD"
                    ]
                  }
                },
                {
                  "when": {
                    "is": "set",
                    "option": "WHL-2SD"
                  },
                  "then": {
                    "update": [
                      {
                        "disabled": true,
                        "option": "SWH-0A1"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0A2"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-0AD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-1RD"
                      },
                      {
                        "disabled": true,
                        "option": "SWH-2SS"
                      },
                      {
                        "disabled": false,
                        "option": "SWH-2SD"
                      }
                    ],
                    "unselect": [
                      "SWH-0A1",
                      "SWH-0A2",
                      "SWH-0AD",
                      "SWH-1RD",
                      "SWH-2SS",
                      "SWH-2SD"
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-C01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-1RD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "260+",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-C01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A1"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-C01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A2"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-C01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0AD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-C01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SS"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-C01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-1RD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A1"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A2"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0AD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SS"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-1RD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "328",
                        "spec": "range"
                      },
                      {
                        "value": "true",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A1"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "289",
                        "spec": "range"
                      },
                      {
                        "value": "true",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A2"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "289",
                        "spec": "range"
                      },
                      {
                        "value": "true",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0AD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "289",
                        "spec": "range"
                      },
                      {
                        "value": "true",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SS"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "303",
                        "spec": "range"
                      },
                      {
                        "value": "true",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-B01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "303",
                        "spec": "range"
                      },
                      {
                        "value": "true",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-1RD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "400",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A1"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A2"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0AD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SS"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-201"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-1RD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "400",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A1"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0A2"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-0AD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SS"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                },
                {
                  "whenAll": [
                    {
                      "is": "set",
                      "option": "BAT-A01"
                    },
                    {
                      "is": "set",
                      "option": "MOT-401"
                    },
                    {
                      "is": "set",
                      "option": "WHL-2SD"
                    }
                  ],
                  "then": {
                    "update": [
                      {
                        "value": "",
                        "spec": "range"
                      },
                      {
                        "value": "false",
                        "spec": "epa"
                      }
                    ]
                  }
                }
              ]
            },
            "basePrice": 67500,
            "version": "2.6",
            "options": [
              {
                "optionId": "BAT-B01",
                "optionName": "Large battery pack",
                "optionDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Large pack"
                    },
                    "gaKey": "Large pack"
                  },
                  "price": 6000,
                  "visualExterior": null,
                  "visualInterior": null,
                  "hidden": null,
                  "disabled": null,
                  "required": null
                },
                "groupId": "BAT",
                "groupName": "Battery",
                "groupDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Battery"
                    },
                    "gaKey": "Range"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "BAT-C01",
                    "BAT-B01",
                    "BAT-A01"
                  ]
                },
                "price": 6000
              },
              {
                "optionId": "EXP-LST",
                "optionName": "Limestone exterior color",
                "optionDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Limestone"
                    },
                    "gaKey": "Limestone Exterior",
                    "genericTitle": {
                      "en-US": "Grey"
                    }
                  },
                  "price": 1750,
                  "visualExterior": true,
                  "visualInterior": true,
                  "hidden": null,
                  "disabled": null,
                  "required": null
                },
                "groupId": "EXP",
                "groupName": "Paint",
                "groupDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Paint"
                    },
                    "gaKey": "Exterior"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "EXP-LGR",
                    "EXP-LSV",
                    "EXP-GWT",
                    "EXP-CRD",
                    "EXP-MDN",
                    "EXP-RBL",
                    "EXP-LST",
                    "EXP-FGR",
                    "EXP-ELG",
                    "EXP-CYL"
                  ]
                },
                "price": 1750
              },
              {
                "optionId": "INT-BMP",
                "optionName": "Black Mountain + Dark Ash Wood interior",
                "optionDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Black Mountain + Dark Ash Wood"
                    },
                    "gaKey": "Black Mountain + Dark Ash Wood interior"
                  },
                  "price": 0,
                  "visualExterior": null,
                  "visualInterior": true,
                  "hidden": null,
                  "disabled": null,
                  "required": null
                },
                "groupId": "INT",
                "groupName": "Interior",
                "groupDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Color options"
                    },
                    "gaKey": "Interior",
                    "longTitle": {
                      "en-US": "Interior"
                    }
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "INT-BMV",
                    "INT-GYV",
                    "INT-BMP",
                    "INT-GYP",
                    "INT-GRP"
                  ]
                },
                "price": 0
              },
              {
                "optionId": "MOT-401",
                "optionName": "Quad-Motor AWD",
                "optionDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Quad-Motor AWD"
                    },
                    "features": [
                      {
                        "key": "drivetrain",
                        "text": {
                          "en-US": "All-wheel drive"
                        }
                      },
                      {
                        "key": "motors",
                        "text": {
                          "en-US": "One motor per wheel"
                        }
                      },
                      {
                        "key": "acceleration",
                        "text": {
                          "en-US": "0–60 mph as quick as 3.0 seconds¹"
                        }
                      },
                      {
                        "key": "power",
                        "text": {
                          "en-US": "More than 800 horsepower"
                        }
                      },
                      {
                        "key": "torque",
                        "text": {
                          "en-US": "More than 900 ft lbs of torque"
                        }
                      }
                    ],
                    "gaKey": "Quad-Motor AWD"
                  },
                  "price": 6000,
                  "visualExterior": null,
                  "visualInterior": null,
                  "hidden": null,
                  "disabled": null,
                  "required": null
                },
                "groupId": "MOT",
                "groupName": "Drive system",
                "groupDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Drive system"
                    },
                    "gaKey": "Motor"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "MOT-201",
                    "MOT-401"
                  ]
                },
                "price": 6000
              },
              {
                "optionId": "ORD-AD3",
                "optionName": "Tow Hooks",
                "optionDetails": {
                  "name": null,
                  "attrs": {
                    "requiredNote": {
                      "en-US": "Included with package"
                    },
                    "description": {
                      "en-US": "Dual, front bumper tow hooks make for quick and easy towing off the beaten path."
                    },
                    "title": {
                      "en-US": "Tow Hooks"
                    },
                    "gaKey": "Tow Hooks"
                  },
                  "price": 0,
                  "visualExterior": true,
                  "visualInterior": null,
                  "hidden": true,
                  "disabled": null,
                  "required": null
                },
                "groupId": "ACCESSORIES",
                "groupName": "Accessories",
                "groupDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Adventure Gear"
                    },
                    "gaKey": "Accessories"
                  },
                  "multiselect": true,
                  "required": false,
                  "options": [
                    "ORD-AD2",
                    "ORD-AD3",
                    "SWH-0A1",
                    "SWH-0A2",
                    "SWH-0AD",
                    "SWH-1RD",
                    "SWH-2SS",
                    "SWH-2SD",
                    "ACERORB001",
                    "ACERAWM002",
                    "ACERRK0001",
                    "ACERFK0003",
                    "TON-M01",
                    "TON-P01",
                    "ACERKSU001",
                    "ACERRTT001",
                    "ACERRTT002",
                    "ACERGTS001",
                    "ACERCSB003",
                    "ACERBM0001",
                    "ACERSSM001",
                    "ACERKM0001",
                    "ACERSM0001",
                    "ACERCWB001",
                    "ACERWC0003",
                    "ACERORM001"
                  ]
                },
                "price": 0
              },
              {
                "optionId": "PKG-ADV",
                "optionName": "Adventure Package",
                "optionDetails": {
                  "name": null,
                  "attrs": {
                    "features": [
                      {
                        "key": "gearGuard",
                        "text": {
                          "en-US": "Gear Guard security cable"
                        }
                      },
                      {
                        "key": "compressor",
                        "text": {
                          "en-US": "Air compressor"
                        }
                      },
                      {
                        "key": "towhooks",
                        "text": {
                          "en-US": "Dual front bumper tow hooks"
                        }
                      },
                      {
                        "key": "sound",
                        "text": {
                          "en-US": "Rivian Elevation audio by Meridian"
                        }
                      },
                      {
                        "key": "leather",
                        "text": {
                          "en-US": "Perforated vegan leather seating with patterned stitching"
                        }
                      },
                      {
                        "key": "seats",
                        "text": {
                          "en-US": "Heated and ventilated seats"
                        }
                      },
                      {
                        "key": "steering",
                        "text": {
                          "en-US": "Heated steering wheel"
                        }
                      },
                      {
                        "key": "lumbarAdj",
                        "text": {
                          "en-US": "Driver and passenger lumbar adjustment"
                        }
                      },
                      {
                        "key": "accents",
                        "text": {
                          "en-US": "Compass Yellow interior accents"
                        }
                      },
                      {
                        "key": "headliner",
                        "text": {
                          "en-US": "100% recycled microfiber headliner"
                        }
                      },
                      {
                        "key": "floormats",
                        "text": {
                          "en-US": "Chilewich floor mats"
                        }
                      }
                    ],
                    "title": {
                      "en-US": "Adventure"
                    },
                    "gaKey": "Adventure Package",
                    "longTitle": {
                      "en-US": "Adventure Package"
                    }
                  },
                  "price": 5500,
                  "visualExterior": true,
                  "visualInterior": true,
                  "hidden": null,
                  "disabled": null,
                  "required": null
                },
                "groupId": "PKG",
                "groupName": "Package",
                "groupDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Package"
                    },
                    "gaKey": "Trim"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "PKG-LCH",
                    "PKG-ADV"
                  ]
                },
                "price": 5500
              },
              {
                "optionId": "RGN-USA",
                "optionName": "United States of America",
                "optionDetails": {
                  "name": null,
                  "attrs": null,
                  "price": 0,
                  "visualExterior": null,
                  "visualInterior": null,
                  "hidden": true,
                  "disabled": null,
                  "required": null
                },
                "groupId": "RGN",
                "groupName": "Region",
                "groupDetails": {
                  "name": null,
                  "attrs": null,
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "RGN-USA"
                  ]
                },
                "price": 0
              },
              {
                "optionId": "WHL-0A1",
                "optionName": "20\" All-Terrain wheel and tire",
                "optionDetails": {
                  "name": null,
                  "attrs": {
                    "description": {
                      "en-US": "Machined aluminum wheel with painted low gloss anthracite."
                    },
                    "title": {
                      "en-US": "20\" All-Terrain"
                    },
                    "gaKey": "20\" All-Terrain Wheels",
                    "longTitle": {
                      "en-US": "20\" All-Terrain wheels"
                    }
                  },
                  "price": 2500,
                  "visualExterior": true,
                  "visualInterior": null,
                  "hidden": null,
                  "disabled": null,
                  "required": null
                },
                "groupId": "WHL",
                "groupName": "Wheels and tires",
                "groupDetails": {
                  "name": null,
                  "attrs": {
                    "title": {
                      "en-US": "Wheels and tires"
                    },
                    "description": {
                      "en-US": "20\" and 22\" wheels reduce estimated range."
                    },
                    "gaKey": "Wheels"
                  },
                  "multiselect": false,
                  "required": true,
                  "options": [
                    "WHL-0A1",
                    "WHL-0A2",
                    "WHL-0AD",
                    "WHL-1RD",
                    "WHL-2SS",
                    "WHL-2SD"
                  ]
                },
                "price": 2500
              }
            ]
          }
        }
      ]
    }
  }
}
```
