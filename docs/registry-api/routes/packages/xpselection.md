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

- "invalid_or_empty_str" -- at least one field which was expected to be a string is not a string, or is an empty string.
- "wrong_repo" -- the provided package identifier is a full identifier that references the wrong repository.
- "invalid_version" -- the provided package version is invalidly formatted.
- "invalid_selection" -- the X-Plane selection provided is invalid.

Sample response:

```text
invalid_or_empty_str
```

## Other Responses

`401`, `409`, `429`, `500`