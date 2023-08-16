# PATCH `/packages/description`

Update the description of a package.

Rate limit: 3 requests every 4 seconds.

## Request 

- Content type: `application/json`
- Authorization: **UpdateDescriptionAnyPackage** | **UpdateDescriptionSpecificPackages**

Request body:

- newDescription
  - Type: `string`
  - Required: **Yes**
  - Description: The new description for the package. Whitespace on the edges will be trimmed. Must be between 10 and 8192 characters long (after whitespace has been trimmed).
- packageId
  - Type `string`
  - Required: **Yes**
  - Description: The full or partial package identifier to update the description of.

Sample request:

```json
{
  "newDescription": "My new and awesome description for my package!",
  "packageId": "example.package2"
}
```

## `204` Response

Sent if the description was updated in the database successfully.

## `400` Response

Sent if the request was invalid.

- Content type: `text/plain`

Response body:

- "no_desc" -- sent if the `newDescription` field is missing from the request body, or if the field value is an invalid type.
- "no_id" -- sent if the `packageId` field is missing from the request body, or if the field value is an invalid type.
- "short_desc" -- sent if the new description is too short.
- "long_desc" -- sent if the new description is too long.
- "invalid_id" -- sent if the package identifier provided is invalid or if the full package identifier refers to a different repository.

Sample response:

```text
missing_form_data
```

## `403` Response

Sent if the author does not own the package with the given package identifier.

## Other responses

`401`, `409`, `429`, `500` 