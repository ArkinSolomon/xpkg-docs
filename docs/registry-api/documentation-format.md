# Documentation Format

The API documentation goes over requests, responses, and status codes for each route. Only significant status codes that may return data, or require clarification are explained, otherwise they will be filed under "Other Responses". These status codes follow [standard HTTP status code definitions](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status). For information on these status codes see the page on [general status codes](/registry-api/status-codes.md). 

The first few pages of this section are general information that applies to the entire registry API, after that all pages are routes. The routes are divided by function (i.e. `/auth/*` routes deal with authorization etc.), and the page will contain all data involving the routes.

Content types will always be provided in the request section of each route. If no request body is to be sent, the content type will be "N/A". Any other content type indicates that a request body may be sent. If a content type is ommitted from the documentation for a response status code, the response data is irrelevant.