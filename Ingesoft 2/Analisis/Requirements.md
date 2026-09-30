1
The text queries and the combined filter application shall return the results in a maximum time of 2 seconds under normal load conditions in a catalog of at least 10,000 clothing items
2
The addition, replacement, or deletion of a garment on the Outfit Builder canvas, as well as the price recalculation of the accumulated total, shall be reflected in the interface in less than 200 milliseconds
3
The catalog images shall be compressed and served in modern formats optimized for the web (WebP, AVIF), with a size of less than 200 KB per image, using lazy loading.
4
The system backend shall support at least 100 active concurrent users browsing and making simultaneous queries without the error rate exceeding 0.5% and without response times degrading by more than 20%
Performance

5
All traffic between clients and servers, as well as communications between microservices or backend processes, shall mandatorily be carried out over the HTTPS protocol with TLS 1.3 encryption
6
Users' passwords shall never be stored in plain text. They must be processed through cryptographic hash functions with a random salt per user using Argon2id or bcrypt with a work factor of at least 12
7
The API authentication shall be implemented with JWT tokens signed with asymmetric algorithms (RS256) or HMAC-SHA256, with a short expiration time (15 minutes).
8
The system shall implement explicit safeguards against common attacks: parameterized queries against SQLi, strict sanitization of inputs and Content Security Policy against XSS, token validation against CSRF, a rate limit of 60 requests/minute per IP address on public endpoints, and a maximum of 5 consecutive failed login attempts before a temporary lockout of 30 minutes.
Security

9
The user interface shall adapt fluidly to different form factors and screen resolutions, offering verified support ranging from compact mobile devices (viewport width of 360px) to high-resolution desktop monitors.
10
The platform shall comply with Web Content Accessibility Guidelines (WCAG 2.1 Level AA), ensuring a minimum color contrast of 4.5:1 for normal text, full keyboard navigation, and semantic attributes (ARIA) for screen readers.
11
Every error or exception on screen shall be translated into a descriptive message in natural language and understandable in Spanish, avoiding exposing stack traces or technical terms to the end user, and indicating the suggested action to resolve it.
Usability

12
The web platform and its API services for end users shall maintain a minimum monthly availability of 99% (only 7.2 hours of downtime per month), excluding maintenance windows notified in advance.
13
Outages, slowdowns, or blocking of scraping operations on an external store shall neither interrupt the rest of the platform's operations nor degrade searches over previously collected data. The extraction workers shall implement exponential backoff and circuit breakers.
14
The system shall execute automatic daily backups of the database and critical configurations. The recovery point objective shall not exceed 24 hours, and the recovery time objective shall be less than 2 hours.
Reliability

15
The system shall be constructed following a modular decoupled architectural pattern (Frontend SPA, Backend RESTful API, independent Scraping, and Database), ensuring that modifications in the scraping adapters do not alter the presentation layer nor the user business logic.
16
Every backend endpoint shall be formally documented under the OpenAPI 3.0 specification, providing an interactive interface detailing routes, HTTP methods, input schemas, status codes, and example responses.
17
The source code shall include automated unit and integration test suites in the Continuous Integration (CI) pipeline, reaching a minimum coverage of 70% over the modules of business logic, authentication, normalization, and price calculation.
Maintainability

18
The web platform shall work correctly and in a consistent way across the latest major versions of the predominant web browsers (Chrome, Firefox, Safari, and Edge), both on desktop operating systems (Windows, macOS, Linux) and mobile (Android, iOS).
19
The client-server communication shall exclusively use the standard JSON format with UTF-8 encoding, complying with standard RESTful conventions for HTTP verbs and status codes.
Compatibility

20
All solution components (web services, extraction workers, and databases) shall be packaged in standard Docker containers, managed through 'docker-compose.yml' files, allowing homogeneous deployment across local development, test, and cloud production environments.
Escalability

21
Given that the system manages prices in COP and serves local and international users, it shall strictly comply with the Colombian General Personal Data Protection Regime (Law 1581 of 2012) and equivalent principles of the GDPR, requiring express authorization prior to personal data processing, providing a visible Information Processing Policy, and allowing the updating, rectification, and suppression of data at the request of the data subject (RF-05, RF-06).
22
The automated catalog collection processes shall respect concurrency policies and the non-saturation of target servers (implementing delays between requests), identifying themselves through a descriptive institutional 'User-Agent' header, not collect protected data through private authentication without authorization, and display clear warnings on the platform that brands and images belong to their respective businesses.
Compliance & Privacy
