# Week 7 Fix Log

## Fix-now
- Added robust contact-form validation for empty, malformed and undersized inputs.
- Added rapid-submit protection by disabling the submit button after a valid validation pass.
- Added a hidden honeypot field to catch simple automated spam attempts.
- Added Open Graph metadata for link previews.
- Added Twitter Card metadata for social sharing.
- Added canonical URLs to reduce duplicate-URL ambiguity.
- Added `robots.txt` and `sitemap.xml` for basic discoverability.
- Added a lightweight SVG social-preview asset instead of a large raster image.
- Clarified that the form does not send data and that LinkedIn is the real contact channel.

## Known limitations
- No backend/contact database is used.
- Search indexing cannot be guaranteed immediately after deployment.
- PageSpeed results vary by run/device/network and must be captured from the live URL at submission time.
- Peer/mentor review must be performed by a real reviewer; this package does not fabricate that evidence.
