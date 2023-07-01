# Rate Limits

All routes on the X-Pkg Registry are rate-limited. The amount of requests that can be made is typically unique to each route, though in some cases, multiple routes may share the same rate limit quota. Unless otherwise specified, if all allotted requests are consumed within the given duration, no further requests can be made for three seconds, after which, the rate limit is reset.

For accounts that do not require the authorization header, the ip address is used to identify clients. If the authorization header is required, the author's identifier is used. Trying to make a request to a route that requires an authorization header, but does not contain one will not count against the rate limit.

## Rate Limiting Headers

Rate limit headers are provided for all requests. Any requests that do not count against rate limiting (like not including an authorization token) do not include these headers.

### `Retry-After`

The amount of seconds that the requester should wait before making the next request.

### `X-RateLimit-Limit`

The total amount of requests that can be made per time duration. See the documentation on specific routes for the time duration. This number is also provided in the documentation and will be the same for all requests to the route.

### `X-RateLimit-Remaining` 

The remaining amount of requests that can be made in this time period. 

### `X-RateLimit-Reset`

The ISO date string of when the rate limit is reset.