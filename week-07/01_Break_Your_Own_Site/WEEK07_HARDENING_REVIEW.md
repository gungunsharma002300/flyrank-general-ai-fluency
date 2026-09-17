# Week 7 Hardening Review

## What was deliberately tested
- Empty contact submission
- Garbage/invalid email input
- Short and oversized message input
- Spam honeypot input
- Rapid repeated submission
- Internal navigation and CV/contact routes
- External repository/profile links
- Mobile/responsive behavior carried forward from Week 6

## Triage
### Fix-now
- Contact input validation and feedback
- Duplicate-submit protection
- Basic SEO metadata
- Social preview metadata
- Crawler discovery files
- Clear non-sending contact behavior

### Known limitation
- No backend form delivery
- Search indexing delay is external to the site
- PageSpeed score must be captured from the live environment at submission time
- Human hardening review must be performed by an actual reviewer

## Reviewer checklist
- [ ] Empty form tested on live URL
- [ ] Garbage form tested on live URL
- [ ] Rapid double-submit tested on live URL
- [ ] Every demo/repository link clicked
- [ ] Search-by-name/site checked
- [ ] PageSpeed Insights screenshot attached
- [ ] Mentor/peer review completed
- [ ] Final live URL recorded in submission notes
