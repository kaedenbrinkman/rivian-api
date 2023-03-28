---
title: transactionStatus
parent: Account Endpoints
has_children: false
nav_order: 3
---

# transactionStatus

## Overview

The `transactionStatus` shows transaction details (steps)

`POST https://rivian.com/api/gql/t2d/graphql`

### Request Body

```json
{
  "operationName": "transactionStatus",
  "variables": {},
  "query": "query transactionStatus($orderId: ID!) { transactionStatus(orderId: $orderId) { titleAndReg { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } tradeIn { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } finance { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } delivery { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } insurance { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } documentUpload { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } contracts { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } payment { sourceStatus { status details } consumerStatus { displayOrder current complete locked inProgress notStarted error } } } }"
}
```

### Example Response

```json
{
  "data": {
    "transactionStatus": {
      "titleAndReg": {
        "sourceStatus": {
          "status": "COMPLETED",
          "details": null
        },
        "consumerStatus": {
          "displayOrder": 1,
          "current": false,
          "complete": true,
          "locked": false,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      },
      "tradeIn": {
        "sourceStatus": {
          "status": "DONE_NOT_WANTED",
          "details": {
            "offer": null
          }
        },
        "consumerStatus": {
          "displayOrder": 2,
          "current": false,
          "complete": true,
          "locked": false,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      },
      "finance": {
        "sourceStatus": {
          "status": "LOAN_APPROVAL_DOC_APPROVED",
          "details": {}
        },
        "consumerStatus": {
          "displayOrder": 3,
          "current": false,
          "complete": true,
          "locked": false,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      },
      "delivery": {
        "sourceStatus": {
          "status": "INIT",
          "details": null
        },
        "consumerStatus": {
          "displayOrder": 8,
          "current": false,
          "complete": false,
          "locked": true,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      },
      "insurance": {
        "sourceStatus": {
          "status": "IN_PROGRESS_POI_UPLOADED",
          "details": {
            "auto": "NOT_VISITED",
            "home": "NOT_VISITED",
            "tenant": "NOT_VISITED",
            "umbrella": "NOT_VISITED",
            "thirdParty": "IN_PROGRESS_POI_UPLOADED"
          }
        },
        "consumerStatus": {
          "displayOrder": 4,
          "current": false,
          "complete": true,
          "locked": false,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      },
      "documentUpload": {
        "sourceStatus": {
          "status": "DOCUMENTS_PENDING_APPROVAL",
          "details": {"Submitted":2,"Approved":2}
        },
        "consumerStatus": {
          "displayOrder": 5,
          "current": false,
          "complete": true,
          "locked": false,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      },
      "contracts": {
        "sourceStatus": {
          "status": "CONTRACTS_SIGNING_COMPLETE",
          "details": {
            "PACKAGE_COMPLETE": "PurchaseAgreement, EDRConsent"
          }
        },
        "consumerStatus": {
          "displayOrder": 6,
          "current": false,
          "complete": true,
          "locked": false,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      },
      "payment": {
        "sourceStatus": {
          "status": "PAYMENT_PROCESSING",
          "details": {
            "statuses": [
              {
                "status": "NO_PAYMENT_SUBMITTED",
                "paymentMethod": null,
                "timestamp": "<timestamp>"
              }
            ]
          }
        },
        "consumerStatus": {
          "displayOrder": 7,
          "current": false,
          "complete": true,
          "locked": false,
          "inProgress": false,
          "notStarted": false,
          "error": false
        }
      }
    }
  }
}
```
