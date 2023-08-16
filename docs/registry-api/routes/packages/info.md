# GET `/info/:packageId/:version`

Get detailed information about a specific package version.

Rate limit: 10 requests every 2 seconds.

## Request

- Content type: N/A
- Authorization: **None**

Route parameters:

- `packageId` -- the partial identifier of the package to get the information of.
- `version` -- the version of the package to get the information of.

Sample route:

```uri
https://registry.xpkg.net/pacakges/info/example.package1/1.8.2a52
```

## `200` Response

Sent if the package exists.

Content type: `application/json`

Response body: 

- loc
  - Type: `string`
  - Required: **Yes**
  - Description: A URI from which to download the package.
- hash
  - Type: `string`
  - Required: **Yes**
  - Description: The SHA256 hash of the X-Pkg file.

Sample response:

```json
{
  "loc": "https://d2cbjuk8vv1874.cloudfront.net/_40fZRpg5ZfQ7j_ANZ5J06-9Mz4QSycT5tSQ4WoVloilYOarVgYBSOQF3yENutSZ",
  "hash": "37dce52e27cbf572bd391d15ff891ae1a27ea7031166e5c86ed1e4f7e48d68a9",
  "dependencies": [
    ["example.package2", "1.2-"]
  ],
  "incompatibilities": []
}
```

## `400` Response

Sent if the package identifier or the package version is invalid.

## Other Responses

`404`, `409`, `429`, `500`