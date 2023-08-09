# GET `/info/:packageId/:version`

Get detailed information about a specific package version.

Rate limit: 10 requests every 2 seconds.

## Request

- Content type: N/A
- Authorization: **None**

Route parameters:

- `packageId` -- The id of the package to get the information of.
- `version` -- The version of the package to get the information of.

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
- dependencies
  - Type: `[string, string][]`
  - Required: **Yes**
  - Description: An array of tuples, where the first element of each tuple is the id of the package which is a dependency, and the second element is the version selection string that the dependency must satisfy.
- incompatibilities
  - Type: `[string, string][]`
  - Required: **Yes**
  - Description: An array of tuples, where the first element of each tuple is the id of the package which is incompatbile, and the second element is the version selection string of all versions that are incompatible.

Sample response:

***TODO***

## `400` Response

Sent if the package identifier or the package version is invalid.

## Other Responses

`404`, `409`, `429`, `500`