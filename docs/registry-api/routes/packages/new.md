# POST `/packages/new`

Create a new package on the registry. Creating a package does not upload a version.

Rate limit: 3 requests every 5 seconds

## Request

- Content type: `multipart/formdata`
- Authorization: **CreatePackage**

Request body:

- packageId
  - Type: [`PackageType`](/registry-api/enumerations#PackageType)
  - Required: **Yes**
  - Description: The type of package that this will be.
- packageName
  - Type: `string`
  - Required: **Yes**
  - Description: The name of the new package. Must be case-insensitively unique. Whitespace on the edges will be trimmed. Must be between 3 and 32 characters long (inclusive) after whitespace has been trimmed.
- packageId
  - Type: `string`
  - Requied: **Yes**
  - Description: The identifier of the new package. Whitespace on the edges will be trimmed, and will be converted to lowercase. Must be between 6 and 32 characters long (inclusive).
- description
  - Type: `string`
  - Required: **Yes**
  - Description: The description of the new package. Whitespace on the edges will be trimmed. Must be between 10 and 8192 characters long (inclusive).

Sample request:

```formdata
------WebKitFormBoundaryxX57CHpQyB1OifNF
Content-Disposition: form-data; name="packageId"

example.package3
------WebKitFormBoundaryxX57CHpQyB1OifNF
Content-Disposition: form-data; name="packageName"

Example Package 3
------WebKitFormBoundaryxX57CHpQyB1OifNF
Content-Disposition: form-data; name="packageType"

other
------WebKitFormBoundaryxX57CHpQyB1OifNF
Content-Disposition: form-data; name="description"

Another cool example package!
------WebKitFormBoundaryxX57CHpQyB1OifNF--
```

## `204` Response

Sent if the package was successfully registered in the database. 

## `400` Response

Sent if the request was invalid.

- Content type: `text/plain`

Response body:

- "missing_form_data" -- form data is missing, or has invalid types.
- "invalid_package_type" -- the `packageType` field does not contain a valid enumeration value.
- "short_id" -- the package identifier is too short.
- "long_id" -- the package identifier is too long.
- "invalid_id" -- the package identifier is invalid.
- "short_name" -- the package name is too short.
- "long_name" -- the package name is too long.
- "short_desc" -- the provided description is too short.
- "long_desc" -- the provided description is too long.
- "profane_id" -- the package identifier was detected to contain profanity.
- "profane_name" -- the package name was detected to contain profanity.
- "profane_desc" -- the package description was detected to contain profanity.
- "id_in_use" -- the package identifier is already in use.
- "name_in_use" -- the package name is already in use.

Sample response:

```text
id_in_use
```

## Other Responses

`401`, `409`, `429`, `500`