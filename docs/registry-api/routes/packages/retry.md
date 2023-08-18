# POST `/packages/retry`

Attempt to reupload a file to a failed version.

Rate limit: 3 requests every 8 seconds.

## Request

- Content type: `multipart/formdata`
- Authorization: **UploadVersionAnyPackage** | **UploadVersionSpecificPackages**

Request body:

- packageId
  - Type: `string`
  - Required: **Yes**
  - Description: The full or partial identifier of the package to reupload the version to.
- packageVersion
  - Type: `string`
  - Required: **Yes**
  - Description: The version string of the version to reupload to.
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

- "missing_form_data" -- form data is missing, or has invalid types.
- "no_file" -- no file was uploaded.
- "short_id" -- the provided package identifier is too short.
- "long_id" -- the provided package identifier is too long.
- "invalid_id" -- the provided package identifier is invalid.
- "no_version" -- no package version was provided (a blank string).
- "long_version" -- the package version provided is too long.
- "invalid_version" -- the package version provided is invalidly formatted.
- "version_not_exist" -- the package version provided does not exist on the package, meaning no job was failed that had to be retried.

## Other Responses

`401`, `409`, `429`, `500`