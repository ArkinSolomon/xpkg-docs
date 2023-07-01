# Status Codes

This page contains general status codes that are not explained in the documentation all the time. They typically follow [standard HTTP status code definitions](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status), however, some routes may provide additional information with or clarification on these status codes, and will be explained there. If no response body for a route is described, the contents of the response are irrelevant.

## Status Code `200`

Any responses with status code 200 will be further explained.

## Status Code `204`

The response was successful, but no content was given.

## Status Code `400`

The are request was missing form fields, or had invalid data passed into it. Sometimes will contain information indicating what is invalid or missing.

## Status Code `401`

The requester was not authorized to perform an action. An authorization token may be required.

## Status Code `403`

Typically sent when an requestor is not allowed to perform a certain action, though they may be authorized.

## Status Code `409`

See the page on [rate limits](/registry-api/rate-limits.md) for information about this status code.

## Status Code `418` 

This response is sent if a route protected by reCAPTCHA assumes you are a bot.

## Status Code `429`

See the page on [rate limits](/registry-api/rate-limits.md) for information about this status code.

## Status Code `500`

The server had an error. This is typically not the requester's fault.