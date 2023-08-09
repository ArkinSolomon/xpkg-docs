# GET `/packages`

Retrieve all packages on the registry that have public versions that have been processed.

Rate limit: 4 requests every 4 seconds.

## Request

- Content type: N/A
- Authorization: **None**

## `200` Response

Sent on every request that does not exceed the rate limit. Contains information about all packages on the registry.

- Content type: `application/json`

Response body:

- data
  - Type: `object[]`
  - Required: **Yes**
  - Description: All of the registry packages, and their versions.
    - packageId
      - Type: `string`
      - Required: **Yes**
      - Description: The identifier of the package.
    - packageName
      - Type: `string`
      - Required: **Yes**
      - Description: The human readable name of the package.
    - authorId
      - Type: `string`
      - Required: **Yes**
      - Description: The identfier of the author.
    - authorName
      - Type: `string`
      - Required: **Yes**
      - Description: The current name of the author.
    - description
      - Type: `string`
      - Required: **Yes**
      - Description: The description of the package.
    - packageType
      - Type: [`PackageType`](/registry-api/enumerations.md#PackageType)
      - Required: **Yes**
      - Description: The type of the package.
    - versions
      - Type: `string[]`
      - Required: **Yes**
      - Description: An array of all of the available versions of the package.

Sample response:

```json
{
  "data": [
    {
      "packageId": "example.package1",
      "packageName": "Example Package 1",
      "authorId": "GPew5C4M1688712972",
      "authorName": "Example Account",
      "description": "A cool example package!",
      "packageType": "other",
      "versions": [
        "1.2.3",
        "1.2.1",
        "1.0.0a-4"
      ]
    }
  ]
}
```

## Other Responses

`409`, `429`