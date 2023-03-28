---
title: EnrollPhone
parent: Vehicle Controls
grand_parent: App API
has_children: false
nav_order: 1
---

# EnrollPhone

## Overview

The `EnrollPhone` endpoint is used to set up a new phone key. Only 2 phones can be enrolled at a time.

## Generating a Key Pair
The first step is to generate an ECDH key pair using the `secp256r1` curve. The public key will be sent to the server, and the private key will be used to sign the HMAC for each command.

Below is an example of generating a key pair using the `cryptography` Python library. You can also use the `openssl` command line tool to generate a key pair.

```python
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Generate a private key
private_key = ec.generate_private_key(ec.SECP256R1())

# Get the corresponding public key
public_key = private_key.public_key()

# Serialize the keys in the standard format
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)
public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print("Private key:", private_key_bytes.decode())
print("Public key:", public_key_bytes.decode())
```

You need to register this public key with Rivian when enrolling your device. This lets Rivian verify that the commands you send are signed with the private key that corresponds to the public key you registered.

`POST https://rivian.com/api/gql/gateway/graphql`

### Required Headers

```text
a-sess: <your app session token>
u-sess: <your user session token>
csrf-token: <your CSRF token>
```

### Request Body

```json
{
  "operationName": "EnrollPhone",
  "variables": {
    "attrs": {
      "userId": <your-user-id>,
      "vehicleId": <your-vehicle-id>,
      "publicKey": <your-phone-public-key>,
      "type": <your-phone-model>,
      "name": <your-phone-name>
    }
  },
  "query": "mutation EnrollPhone($attrs: EnrollPhoneAttributes!) { enrollPhone(attrs: $attrs) { __typename success } }"
}
```

### Example Response

```json
{
  "data": {
    "enrollPhone": {
      "__typename": "EnrollPhoneResponse",
      "success": true
    }
  }
}
```
