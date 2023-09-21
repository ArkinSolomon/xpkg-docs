# Authorization Tokens

**Authorization tokens** cover both the tokens issued when an author logs in to the developer portal, and any [API tokens](package-developers/api-tokens.md) that are issued. They are both JWTs and both have the same payload schema.

## Token Payload

The schema of the token's payload is as follows:

- authorId
  - Type: `string`
  - Required: **Yes**
  - Description: The id of the author that owns this token.
- session
  - Type: `string`
  - Required: **Yes**
  - Description: The session of the author.
- permissions
  - Type: `string`
  - Required: **Yes**
  - Description: The [permission number](#permission-numbers) of the token.
- versionUploadPackages
  - Type: `string[]`
  - Required: **Yes** 
  - A list of package identifiers (that the author owns) which the bearer of the token has permission to upload a new version for. Empty if the [UploadVersionSpecificPackages](/package-developers/api-tokens#UploadVersionSpecificPackages) permission is not granted.
- descriptionUpdatePackages
  - Type: `string[]`
  - Required: **Yes** 
  - A list of package identifiers (that the author owns) which the bearer of the token has permission to update the description of. Empty if the [UpdateDescriptionSpecificPackages](/package-developers/api-tokens#UpdateDescriptionSpecificPackages) permission is not granted.
- updateVersionDataPackages
  - Type: `string[]`
  - Required: **Yes** 
  - A list of package identifiers (that the author owns) which the bearer of the token has permission to update the version data of of. Empty if the [UpdateVersionDataSpecificPackages](/package-developers/api-tokens#UpdateVersionDataSpecificPackages) permission is not granted.
- viewAnalyticsPackages
  - Type: `string[]`
  - Required: **Yes** 
  - A list of package identifiers (that the author owns) which the bearer of the token has permission to update the version data of of. Empty if the [ViewAnalyticsSpecificPackages](/package-developers/api-tokens#ViewAnalyticsSpecificPackages) permission is not granted.
- tokenSession
  - Type: `string`
  - Required: **No**
  - Description: The session of the token. Only provided on issued tokens (see next section).

## Admin Tokens & Issued Tokens

Authorization tokens that are recieved on author login (or account creation) may be referred to as **admin tokens**. These tokens are the only tokens that can have the admin permission (see [Permission Numbers](#permission-numbers) for clarification). **API tokens**, that is, tokens issued via the developer portal (or the [`/auth/issue`](/registry-api/routes/auth/issue) route) may also be referred to as **issued tokens**. Remember that "authorization tokens" refer to both types.

## Author Sessions & Token Sessions

There are two different sessions provided, the **author session** (`authorSession`) and the **token session** (`tokenSession`). These sessions are used to validate/revoke the tokens. If either session does not match the session in the database, the token is considered invalid. This way, even unexpired tokens can be revoked. 

The author session is always provided for every authorization token. The author session is reset on every password reset. This immediately invalidates all authorization tokens. Token sessions are more like ids, they are unique, and issued tokens are referenced with their sessions. Token sessions can be revoked using the ***`TODO`*** route.

## Permission Numbers

Every token has a permission number, which is an 11-bit integer that specifies what the token is permitted to do. It is a bitwise flag, meaning that every bit means a different permission. A set bit means the permission is granted, and an unset bit means the permission is not granted. A permission number less than or equal to zero is invalid. 

On top of the permissions covered [here](package-developers/api-tokens.md). There is also the Admin permission. This permission is only granted to admin tokens. API Routes that require the Admin permission are typically sensitive, and require a human to perform them. The admin token also implicitly grants every other permission.

Here is every permission along with its offset:

| Permission                        | Offset |
| --------------------------------- | :----: |
| Admin                             |   0    |
| CreatePackage                     |   1    |
| UploadVersionAnyPackage           |   2    |
| UpdateDescriptionAnyPackage       |   3    |
| UploadVersionSpecificPackages     |   4    |
| UpdateDescriptionSpecificPackages |   5    |
| UploadResources                   |   6    |
| ReadAuthorData                    |   7    |
| UpdateAuthorData                  |   8    |
| ViewPackages                      |   9    |
| ViewResources                     |   10   |
| UpdateVersionDataAnyPackage       |   11   |
| UpdateVersionDataSpecificPackages |   12   |

## Example

Consider the following authorization token:

```text
eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJ0b2tlblNlc3Npb24iOiJlR2lFeTgxdTh1cXFwcjNiYWJFRFIiLCJzZXNzaW9uIjoiVlU2enlyTXpROFRJMkRJbXh6dWVCIiwiYXV0aG9ySWQiOiJHUGV3NUM0TTE2ODg3MTI5NzIiLCJwZXJtaXNzaW9ucyI6NjU4LCJkZXNjcmlwdGlvblVwZGF0ZVBhY2thZ2VzIjpbXSwidmVyc2lvblVwbG9hZFBhY2thZ2VzIjpbImV4YW1wbGUucGFja2FnZTEiLCJleGFtcGxlLnBhY2thZ2UyIl0sImlhdCI6MTY4OTIzMDE0OSwiZXhwIjoxNjk0NDE0MTQ5fQ.LBOeLb-zmKJkqR26umKBtHyu9rW516G2UEyHlew3sibui8g3VDPLX7RAJ2v9EXQ4
```

Its payload is as follows:

```json
{
  "tokenSession": "eGiEy81u8uqqpr3babEDR",
  "session": "VU6zyrMzQ8TI2DImxzueB",
  "authorId": "GPew5C4M1688712972",
  "permissions": 658,
  "descriptionUpdatePackages": [],
  "versionUploadPackages": [
    "example.package1",
    "example.package2"
  ],
  "updateVersionDataPackages": []
}
```

Since the token sesssion is provided, we know that this is an API token. The permissions number (658) in binary is as follows:

```text
0 0 0 1 0 1 0 0 1 0 0 1 0 = 658
│ │ │ │ │ │ │ │ │ │ │ │ └─ Admin (not set)
│ │ │ │ │ │ │ │ │ │ │ └─── CreatePackage (set)
│ │ │ │ │ │ │ │ │ │ └───── UploadVersionAnyPackage (not set)
│ │ │ │ │ │ │ │ │ └─────── UpdateDescriptionAnyPackage (not set)
│ │ │ │ │ │ │ │ └───────── UploadVersionSpecificPackages (set)
│ │ │ │ │ │ │ └─────────── UpdateDescriptionSpecificPackages (not set)
│ │ │ │ │ │ └───────────── UploadResources (not set)
│ │ │ │ │ └─────────────── ReadAuthorData (set)
│ │ │ │ └───────────────── UpdateAuthorData (not set)
│ │ │ └─────────────────── ViewPackages (set)
│ │ └───────────────────── ViewResources (not set)
│ └─────────────────────── UpdateVersionDataAnyPackage (not set)
└───────────────────────── UpdateVersionDataSpecificPackages (not set)
```

After decoding the permissions number, we can see that this token has permission to create packages, upload new versions to the packages `example.package1` and `example.package2`, as well as viewing the author's account information, as well as listing all of the author's packages.