# PATCH `/packages/incompatibilities`

Update the incompatibilities for a specific package version.

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
  - Description: The version fo the package to update the incompatibilities of.
- incompatibilities
  - Type: `[string, string][]`
  - Required: **Yes**
  - Description: An array of tuples of incompatibilities, where the first value is the identifier of the incompatibility, and the second value is the version selection which is incompatible. Overwrite all incompatibilities with these values. Duplicates will be merged. Maximum length of 128.

Sample request:

```json
{
  "packageId": "example.package1",
  "version": "4.2.1",
  "incompatibilities": [
    ["example.package2", "*"],
    ["randomauthor.package1", "1.2-3.4"]
  ]
}
```

## `204` Response

Response sent if the incompatibilities were successfully updated.

## `400` Response

Response sent if the request is invalid.

- Content type: `text/plain`

Response body:

- "invalid_form_data" -- sent the request body is missing required fields, or if they are the wrong type.
- "too_many_incompatibilities" -- sent if the provided incompatibility list is too long.
- "invalid_id" -- sent if the provided package identifier is invalid, or if the identifier references another repository.
- "invalid_version" -- sent if the provided package version is formatted invalidly.
- "bad_inc_tuple" -- sent if the provided incompatibility list has an element in the list that is either not a JSON array, or is a JSON array that does not have a length of two.
- "invalid_inc_tuple_types" -- sent if the provided incompatibility list has a tuple in the list where at least one element is not a string.
- "invalid_inc_tuple_id" -- sent if the provided incompatibility list has a tuple in the list where the package identifier is invalid.
- "dep_or_self_inc" -- sent if the provided incompatibility list declares itself to be incompatibile with itself or with a dependency.
- "invalid_inc_sel" -- sent if the provided incompatibility list contains a selection that is invalid.

## `401` Response

Response sent if the provided token does not have valid authorization to update the version data of a package. Response may also be sent if the package at the specified version is not found.

## Other Responses

`409`, `429`, `500`