# Week 7 — Break Your Own Site

## Assignment
Hardening review of the public portfolio: deliberately test edge cases, improve findability and basic SEO, run a speed check, triage findings into **fix-now** and **known limitation**, fix the fix-now items, and document the evidence.

## Site under test
Production: https://flyrank-general-ai-fluency.vercel.app/
Source: GitHub repository `flyrank-general-ai-fluency`

## Fix-now items completed in this package
1. **No real contact-form test surface** → added a client-side contact form with required fields, email validation, length limits, visible error messages, spam honeypot, and duplicate-submit protection.
2. **Missing social-share metadata** → added Open Graph and Twitter Card metadata to the main, contact and CV pages.
3. **Missing canonical metadata** → added canonical URLs to the public HTML pages.
4. **Missing crawler files** → added `robots.txt` and `sitemap.xml`.
5. **No explicit social-preview asset** → added `social-preview.svg` and referenced it from OG/Twitter metadata.
6. **Contact behavior could be misleading** → clearly labels the form as local validation only and directs real contact to LinkedIn; no fake successful message delivery is claimed.

## Deliberate break tests
| Test | Expected behavior | Evidence status |
|---|---|---|
| Empty contact form | Required-field errors; no success state | Code-level verification completed; manual live screenshot should be captured by submitter |
| Garbage email | Email validation error; no success state | Code-level verification completed; manual live screenshot should be captured by submitter |
| Very short message | Minimum-length error | Code-level verification completed |
| Oversized message | Maximum-length error | Code-level verification completed |
| Spam honeypot filled | Submission blocked | Code-level verification completed |
| Double-click / rapid second submit | Button disabled briefly after valid validation | Code-level verification completed |
| Internal CV/contact routes | Pages should resolve | Local static audit completed |
| External GitHub/LinkedIn links | Open in a new tab with `noopener noreferrer` | Static link audit completed |

## Known limitations
- The contact form is intentionally **front-end only**. It does not send or store messages. LinkedIn remains the actual contact channel.
- Search-engine indexing is outside the repository's immediate control. A new Vercel URL may not appear in search immediately.
- A real PageSpeed Insights run and a real mentor/peer hardening review require the submitter's browser/account interaction; no score or review outcome is fabricated in this package.

## Review principle
Only observed or code-verifiable findings are recorded as completed. Search ranking, PageSpeed scores, physical-device observations, and peer-review outcomes are not invented.
