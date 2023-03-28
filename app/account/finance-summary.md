---
title: financeSummary
parent: Account Endpoints
has_children: false
nav_order: 3
---

# transactionStatus

## Overview

The `financeSummary` shows financing details

`POST https://rivian.com/api/gql/t2d/graphql`

### Request Body

```json
{
  "operationName": "financeSummary",
  "variables": {},
  "query": "query financeSummary($orderId: ID!) { ...FinanceSummaryFragment } fragment FinanceSummaryFragment on Query { financeSummary(orderId: $orderId) { orderId status financeChoice { financeChoice institutionName paymentMethod trackingNumber preApprovedAmount loanOfficerName loanOfficerContact downPayment rate term rateAndTermSkipped } } }"
}
```

### Example Response

```json
{
  "data": {
    "financeSummary": {
      "orderId": "<order id>",
      "status": "LOAN_APPROVAL_DOC_APPROVED",
      "financeChoice": {
        "financeChoice": "EXTERNAL_FINANCING",
        "institutionName": "<your bank name>>",
        "paymentMethod": "ACH",
        "trackingNumber": null,
        "preApprovedAmount": "USD 90000.00",
        "loanOfficerName": null,
        "loanOfficerContact": null,
        "downPayment": "USD 10000.00",
        "rate": 5.00,
        "term": 60,
        "rateAndTermSkipped": false
      }
    }
  }
}
```
