# PATCH `/packages/xpselection` 

Update the X-Plane selection of a package version.

Rate limit: 3 requests every 4 seconds.

## Request

- Content type: `application/json`
- Authorization: **UpdateVersionDataAnyPackage** | **UpdateVersionDataSpecificPackages**

Request body:

- packageId
  - Type: `string`
  - Required: **Yes**
  - Description: The full or partial identifier of the package to update the incompatibilities of.
- version
  - Type: `string`
  - Required: **Yes**
  - Description: The version of the package to update the incompatibilities of.
- xpSelection
  - Type: `string`
  - Required: **Yes**
  - Description: The new X-Plane selection. Maximum length of 256 characters.

Sample request:

```json
{
  "packageId": "example.package1",
  "version": "4.2.1",
  "xpSelection": "11.6-12.4b4"
}
```

## `204` Response

Response sent if the X-Plane selection was successfully updated in the database.

## `400` Response

- Content type: `text/plain`

Response body: 

- "missing_form_data" -- sent the request body is missing required fields, or if they are the wrong type.
- "short_id" -- sent if the provided incompatibility list is too long.
- "long_id" -- sent if the provided package identifier is too long.
- "invalid_id" -- sent if the provided package identifier is invalid, or if the identifier references another repository.
- "no_version" -- sent if the `version` field is just an empty string.
- "long_version" -- sent if the `version` field is too long.
- "invalid_version" -- sent if the provided package version is invalidly formatted.
- "empty_xp_sel" -- the X-Plane version selection string is empty.
- "long_xp_sel" -- the X-Plane version selection string is too long.
- "invalid_xp_sel" -- the X-Plane version selection string is invalid.

Sample response:

```text
missing_form_data
```

## Other Responses

`401`, `409`, `429`, `500`