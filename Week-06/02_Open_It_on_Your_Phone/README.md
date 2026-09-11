# FlyRank Week 6 — Open It on Your Phone

## Gungun Sharma Personal Portfolio

This package contains the revised static portfolio prepared for FlyRank General AI Fluency Week 6.

### What is included

- `site/index.html` — responsive portfolio homepage
- `site/style.css` — responsive/accessibility styling
- `site/script.js` — accessible mobile navigation
- `site/booking.html` — connect page
- `site/resume.html` — web CV page
- `site/Gungun_Sharma_CV.pdf` — downloadable CV
- `WEEK06_FIX_LOG.md` — before/problem → fix → result log
- `AI_AUDIT.md` — mobile/accessibility/performance audit notes
- `REAL_PHONE_TEST.md` — physical-phone verification checklist
- `evidence/` — reserved for real before/after phone screenshots
- `docs/NETLIFY_DEPLOYMENT.md` — deployment guidance from the earlier portfolio package
- `docs/DNS_WALKTHROUGH.md` — DNS notes from the earlier portfolio package

### Run locally

Because this is a static site, no build step is required.

From the `site` folder, serve the files with any static HTTP server. For example with Python:

```powershell
cd site
python -m http.server 8000
```

Then open `http://localhost:8000`.

### Important submission rule

The FlyRank assignment requires a real-phone test. This package does **not** invent that evidence. After deployment, open the real live URL on a physical phone and complete `REAL_PHONE_TEST.md`. Add genuine before/after phone screenshots to `evidence/` if you have them.

Do not submit the assignment reference URL as the portfolio URL. Submit the final live portfolio URL after it has been tested.
