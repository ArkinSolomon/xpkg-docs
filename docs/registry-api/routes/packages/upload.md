# POST `/packages/upload`

Upload a new package version to the registry.

Rate limit: 3 requests every 8 seconds.

## Request

- Content type: `multipart/formdata`
- Authorization: **UploadVersionAnyPackage** | **UploadVersionSpecificPackages**

Request body:

- packageId
  - Type: `string`
  - Required: **Yes**
  - Description: The id of the package to upload the version to.
- packageVersion
  - Type: `string`
  - Required: **Yes**
  - Description: The version string of the new version.
- xplaneSelection
  - Type: `string`
  - Required: **Yes**
  - Description: The version selection of the compatible X-Plane versions. May not be longer than 256 characters.
- isPublic
  - Type: `boolean`
  - Required: **Yes**
  - Description: True if the package version is public. Can not be true if `isPrivate` is true, or if `isStored` is false.
- isPrivate
  - Type: `boolean`
  - Required: **Yes**
  - Description: True if the package version is public. Can not be true if `isPublic` is true.
- isStored
  - Type: `boolean`
  - Required: **Yes**
  - Description: True if the package version should be permanently stored on X-Pkg servers. Can not be false if `isPublic` is true.
- dependencies
  - Type: `STR<[string, string][]>`
  - Required: **Yes**
  - Description: A JSON string which is an array of tuples, where the first element of each tuple is the id of the package which is a dependency, and the second element is the version selection string that the dependency must satisfy.
- incompatibilities
  - Type: `STR<[string, string][]>`
  - Required: **Yes**
  - Description: A JSON string which is an array of tuples, where the first element of each tuple is the id of the package which is incompatbile, and the second element is the version selection string of all versions that are incompatible.
- file
  - Type: `file`
  - Required: **Yes**
  - Description: The .zip file of the package. See the [folder structure of a package](/package-developers/packaging.md) for information on the file's contents.

Sample request:

```formdata
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="packageId"

example.package1
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="packageVersion"

1.3b9
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="xplaneSelection"

*
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="isPublic"

true
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="isPrivate"

false
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="isStored"

true
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="dependencies"

[["example.package2","1.2-"]]
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="incompatibilities"

[]
------WebKitFormBoundaryc5i0j0B6oJS681gS
Content-Disposition: form-data; name="file"; filename="Example Package.zip"
Content-Type: application/zip

PK|ð...the file...PK`
------WebKitFormBoundaryc5i0j0B6oJS681gS--
```

## `204` Response

Response sent if the package has begun processing successfully. Does not mean that the version will process successfully.

## `400` Response

Sent if the request was invalid.

- Content type: `text/plain`

Response body:

- "missing_form_data" -- form data is missing, or has invalid types.
- "no_file" -- no file was uploaded.
- "short_id" -- the provided package identifier is too short.
- "long_id" -- the provided package identifier is too long.
- "invalid_id" -- the provided package identifier is invalid.
- "no_version" -- no package version was provided.
- "long_version" -- the package version provided is too long.
- "invalid_version" -- the package version provided is invalid.
- "invalid_access_config" -- the access configuration (`isPublic`, `isPrivate`, and `isStored` fields) was invalid.
- "empty_xp_sel" -- the X-Plane version selection string is empty.
- "long_xp_sel" -- the X-Plane version selection string is too long.
- "invalid_xp_sel" -- the X-Plane version selection string is invalid.
- "vesion_exists" -- the package with the given identifier already has the specified version.

## `403` Response

Sent if the author does not own the package with the provided identifier.

## Other Responses

`401`, `409`, `429`, `500`