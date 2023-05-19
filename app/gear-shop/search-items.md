---
title: SearchShopProductsBySkus
parent: Gear Shop Endpoints
grand_parent: App API
has_children: false
nav_order: 1
---

# SearchShopProductsBySkus

## Overview

The `SearchShopProductsBySkus` endpoint returns the details about products in the Gear Shop from a list of SKUs to fetch.

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
  "operationName": "SearchShopProductsBySkus",
  "variables": {
    "country": "US",
    "skus": [...],
    "pageInfo": {
      "from": 0,
      "size": 106
    }
  },
  "query": "query SearchShopProductsBySkus($country: String! = \"US\", $skus: [String!]!, $pageInfo: ElasticSearchPageInput) {\n  searchProducts(\n    input: {storeType: ONLINE_STORE, country: $country, pageInfo: $pageInfo, filters: {skus: $skus}}\n  ) {\n    total\n    size\n    from\n    data {\n      ...SearchShopProductsChildProduct\n      ...SearchShopProductsStandaloneProduct\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment SearchShopProductsChildProduct on ChildProduct {\n  _id: sku\n  sku\n  title\n  brand\n  rivianShopStatus\n  price {\n    listPrice {\n      amount\n      currency\n      __typename\n    }\n    __typename\n  }\n  dimensionValues {\n    name\n    valueName\n    localizedStrings\n    __typename\n  }\n  channels\n  channelAttributes {\n    ...SearchShopProductsChannelAttribute\n    __typename\n  }\n  __typename\n}\n\nfragment SearchShopProductsChannelAttribute on ChannelAttribute {\n  attributeId\n  name\n  channel\n  value\n  __typename\n}\n\nfragment SearchShopProductsStandaloneProduct on StandaloneProduct {\n  _id: sku\n  sku\n  title\n  brand\n  rivianShopStatus\n  price {\n    listPrice {\n      amount\n      currency\n      __typename\n    }\n    __typename\n  }\n  channels\n  channelAttributes {\n    ...SearchShopProductsChannelAttribute\n    __typename\n  }\n  __typename\n}\n"
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
