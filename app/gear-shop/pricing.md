---
title: SearchShopPricingBySku
parent: Gear Shop Endpoints
grand_parent: App API
has_children: false
nav_order: 2
---

# SearchShopPricingBySku

## Overview

The `SearchShopPricingBySku` endpoint returns the pricing details about products in the Gear Shop from a list of SKUs to fetch.

The SKU is the unique identifier for a product in the Gear Shop. For example, the SKU for the Rivian Camp Kitchen x Snow Peak Package is `ACERRCK001`.

`POST https://rivian.com/api/gql/orders/graphql`

### Required Headers

```text
csrf-token: <your CSRF token>
dc-cid: <your correlation id>
x-datadog-origin: rum
```

### Request Body

```json
{
  "operationName": "SearchShopPricingBySku",
  "variables": {
    "country": "US",
    "skus": [...],
    "pageInfo": {
      "from": 0,
      "size": 250
    }
  },
  "query": "query SearchShopPricingBySku($country: String! = \"US\", $skus: [String!]!, $pageInfo: ElasticSearchPageInput) {\n  searchProducts(\n    input: {storeType: ONLINE_STORE, country: $country, pageInfo: $pageInfo, filters: {skus: $skus}}\n  ) {\n    total\n    data {\n      ...SearchShopPricingChildProduct\n      ...SearchShopPricingStandaloneProduct\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment SearchShopPricingChildProduct on ChildProduct {\n  sku\n  price {\n    listPrice {\n      amount\n      currency\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment SearchShopPricingStandaloneProduct on StandaloneProduct {\n  sku\n  price {\n    listPrice {\n      amount\n      currency\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
}
```

### Example Response

```json
{
  "searchProducts": {
    "total": 106,
    "size": 106,
    "from": 0,
    "data": [...],
    "__typename": "ProductSearch"
  }
}
```
